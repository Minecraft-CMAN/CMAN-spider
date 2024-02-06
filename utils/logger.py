import logging
import datetime
from rich.logging import RichHandler

rich_handler = RichHandler()
file_handler = logging.FileHandler(f'./runtime/logs/{datetime.datetime.now().strftime("%Y-%m-%d_%H")}.log')

file_handler.setFormatter(logging.Formatter('[%(levelname)s - %(asctime)s] %(message)s'))

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[
        rich_handler,
        file_handler
    ]
)