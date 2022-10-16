import asyncio
import dataclasses
from utils.protocol.request import Request


@dataclasses.dataclass
class Connection:
    writer: asyncio.StreamWriter
    token: str

    def send(self, message: Request):
        self.writer.write(message.form_protocol().encode("utf-8"))
        self.writer.drain()
