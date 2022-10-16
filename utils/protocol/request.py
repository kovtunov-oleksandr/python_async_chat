import dataclasses

# TODO: command;;status_code;;sender;;receiver;;auth;;content;;time


@dataclasses.dataclass
class Request:
    command: str
    status_code: str
    sender: str
    receiver: str
    token: str
    content: str
    time: str

    def form_protocol(self):
        return f'{self.command};;{self.status_code};;{self.sender};;{self.receiver};;{self.token};;{self.content};;{self.time}'

