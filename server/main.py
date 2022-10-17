import asyncio
import logging
import sys
from server.config import server
from server import routes

logging.basicConfig(stream=sys.stderr, level=logging.NOTSET,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def main():

    await server.run_server()


if __name__ == '__main__':
    asyncio.run(main())
