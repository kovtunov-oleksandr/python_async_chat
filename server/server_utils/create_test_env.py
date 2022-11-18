import asyncio
from server.config import server
from server import routes # noqa
from server.server_utils.db_utils import recreate_db_force


async def main():

    await recreate_db_force()
    await server.run_server()


if __name__ == "__main__":
    asyncio.run(main())
    