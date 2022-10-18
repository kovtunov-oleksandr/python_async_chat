import asyncio
from utils.protocol import Request, form_timestamp


class Client:

    def __init__(self, HOST, PORT):
        self.session = {'user': '', 'token': ''}
        self.host = HOST
        self.port = PORT
        self.command_map = {}

    async def send(self, writer: asyncio.StreamWriter, data: bytes):
        writer.write(data)
        await writer.drain()

    async def listen(self, reader: asyncio.StreamReader):
        while True:
            data = await reader.read(1024)
            response = data.decode()
            if not response:
                raise Exception("Connection closed")
            return self.decode_protocol(response)

    async def decode_protocol(self, string: str):
        data = string.split(';;')
        request = Request(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        print(request)
        return request

    async def code_client_action(self, request: Request):
        await asyncio.sleep(0.000001)
        return request.form_protocol()     #add to Request func - form_timestamp

    async def handler(self, method: str):
        def inner(func):
            self.command_map[method] = func
        return inner

    async def send_request(self, writer: asyncio.StreamWriter):
        while True:
            request = await self.code_client_action(          # await something from pyQT
                Request(command='01',
                        status_code='0',
                        sender='login',
                        receiver='_',
                        token='_',
                        content='pass',
                        time='_')
            )
            await self.send(writer, request.encode("utf-8"))

    async def start_client(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        await asyncio.gather(self.listen(reader), self.send_request(writer))


if __name__ == '__main__':
    HOST = "localhost"  #TODO: input host addr
    PORT = 5050         #TODO: input port addr
    client = Client(HOST, PORT)
    asyncio.run(client.start_client())


