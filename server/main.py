import asyncio
from server.config.config import server
from server import routes


async def main():

    print(server.command_map)  # TODO: delete after testing, shows that command map is working
    await server.run_server()


if __name__ == '__main__':
    asyncio.run(main())
