import asyncio
from server.config import server
from server import routes


async def main():

    await server.run_server()


if __name__ == '__main__':
    asyncio.run(main())
