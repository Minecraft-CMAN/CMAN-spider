from aiohttp import ClientSession
from typing import List, Dict
from utils.logger import logging

logger = logging.getLogger(__name__)

async def fetch_projects(session: ClientSession) -> List[Dict]:
    # Get total_hits
    newest_resp = await session.get('/v2/search?limit=1&index=newest')
    
    # When error
    if newest_resp.status != 200:
        logger.error(f"Failed to get total hits: {newest_resp.status} {await (newest_resp.json())['error']}")
        return []
    else:
        total_hits = (await (newest_resp.json()))['total_hits']
        logger.info(f"Total hits: {total_hits}")
    
    # Let limit=total_hits
    all = await session.get(f'/v2/search?limit={total_hits}&index=newest')
    
    logger.info(f"Fetched {total_hits} projects")
    
    return (await all.json())['hits']