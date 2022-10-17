import dataclasses


@dataclasses.dataclass
class Message:
    command: str
    status_code: str
    sender: str
    receiver: str
    token: str
    content: str
    time: str

    def form_protocol(self):
        return f'{self.command};;{self.status_code};;{self.sender};;{self.receiver};;' \
               f'{self.token};;{self.content};;{self.time}'
