from utils.protocol.message import Message


def parse_protocol_message(data: str) -> Message:
    data = data.split(';;')
    request = Message(*data)
    return request
