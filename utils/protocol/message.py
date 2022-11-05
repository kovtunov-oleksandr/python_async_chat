import dataclasses
import json


@dataclasses.dataclass
class Message:
    command: str
    sender: str
    receiver: str
    token: str
    content: str

    def form_protocol(self) -> str:
        return f"{self.command};;{self.sender};;{self.receiver};;{self.token};;{self.content}"

    @classmethod
    def parse_protocol_message(cls, data: str):
        data = data.split(";;")
        return cls(*data)

    def encode_content_from_json(self) -> dict:
        return json.loads(self.content)

    @classmethod
    def decode_content_to_json(cls, content) -> str:
        return json.dumps(content)
