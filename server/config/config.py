import asyncio
import dataclasses
from utils.protocol.server import Server

HOST = 'localhost'
PORT = 5050
FORMAT = 'utf-8'

server = Server(HOST, PORT, FORMAT)
