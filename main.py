import asyncio
import apscheduler
import configs
import aiohttp
import datetime
import spider
import threading
import pickle
import modules.mod
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.asyncio import AsyncIOExecutor
from typing import List, Dict, Optional, Literal, Set, Union
from objprint import op
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, TransferSpeedColumn, TimeElapsedColumn, ProgressColumn, MofNCompleteColumn, SpinnerColumn

from utils.logger import logging

logger = logging.getLogger(__name__)


async def main():
    logger.info('CMAN-spider start')

    async with aiohttp.ClientSession(base_url=configs.MODRINTH_BASE_URL) as session:
        projects_unanalyzed = await spider.fetch_projects(session)
        
        logger.info(f'Starting to analyze projects')

        projects = [
            modules.mod.Mod(
                slug=project['slug'],
                title=project['title'],
                description=project['description'],
                client_side=project['client_side'],
                server_side=project['server_side'],
                project_type=project['project_type'],
                downloads=project['downloads'],
                project_id=project['project_id'],
                author=project['author'],
                versions=project['versions'],
                follows=project['follows'],
                date_created=project['date_created'],
                date_modified=project['date_modified'],
                license=project['license'],
                
                categories=project.get('categories', None),
                icon_url=project.get('icon_url', None),
                color=project.get('color', None),
                thread_id=project.get('thread_id', None),
                monetization_status=project.get('monetization_status', None),
                display_categories=project.get('display_categories', None),
                latest_version=project.get('latest_version', None),
                gallery=project.get('gallery', None),
                featured_gallery=project.get('featured_gallery', None),
            )
            for project in projects_unanalyzed
        ]

        logger.info(f"Analyzed projects, starting to fetch projects's versions")
        
        with Progress(
            SpinnerColumn('earth'),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            MofNCompleteColumn()
        ) as progress:
            progress.add_task(total=len(projects), description='Fetching versions', initial=0)
            
            index = 0
            while index <= len(projects):
                start = index
                end = min(index + configs.FETCH_VERSION_MERGE, len(projects) - 1)
                
                # Fetch
                tasks = [x.fetch_project_versions(session) for x in projects[start:end]]
                await asyncio.gather(*tasks)
                
                # Save
                for x in projects[start:end]:
                    pickle.dump(x, open(f"generated/{x.project_id}.mod", "wb"))

                index += configs.FETCH_VERSION_MERGE                
                progress.update(task_id=0, advance=configs.FETCH_VERSION_MERGE)
        
        if logger.level <= logging.DEBUG:
            op(projects)

    logger.info(
        f'CMAN-spider end, next run time at {datetime.datetime.now() + datetime.timedelta(hours=6)}')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    scheduler = AsyncIOScheduler(event_loop=loop)
    scheduler.add_executor(AsyncIOExecutor())

    scheduler.add_job(main, 'interval', hours=6, next_run_time=datetime.datetime.now())

    scheduler.start()
    loop.run_forever()
