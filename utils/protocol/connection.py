import asyncio
import dataclasses
from utils.logger import logger
from utils.protocol.message import Message


@dataclasses.dataclass
class Connection:
    writer: asyncio.StreamWriter

    def send_message(self, message: Message):
        logger.debug(f'Sending to {self.writer.get_extra_info("peername")} data:{message.form_protocol()}')
        self.writer.write(message.form_protocol().encode("utf-8"))
        self.writer.drain()
