import asyncio
import dataclasses
import logging
import sys
from utils.protocol.message import Message

logging.basicConfig(stream=sys.stderr, level=logging.NOTSET,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Connection:
    writer: asyncio.StreamWriter

    def send_message(self, message: Message):
        logger.debug(f'Sending to {self.writer.get_extra_info("peername")} data:{message.form_protocol()}')
        self.writer.write(message.form_protocol().encode("utf-8"))
        self.writer.drain()
