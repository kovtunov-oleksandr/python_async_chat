import datetime
from utils.protocol.message import Message


def form_timestamp():
    return datetime.datetime.now().strftime('%H:%M:%S')


def parse_protocol_message(data: str) -> Message:
    data = data.split(';;')
    request = Message(*data)
    return request
