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


# a = Request('01', '1', 'admin', 'user', '12354', 'helllo bro', '12:00:00')
# print(a.form_protocol())