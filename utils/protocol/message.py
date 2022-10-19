import dataclasses


@dataclasses.dataclass
class Message:
    command: str
    sender: str
    receiver: str
    token: str
    content: str

    def form_protocol(self):
        return f'{self.command};;{self.sender};;{self.receiver};;{self.token};;{self.content}'
