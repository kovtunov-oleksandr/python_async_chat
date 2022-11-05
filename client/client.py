from utils.protocol import Client, Message



class ChatClient(Client):
    async def create_chat(self, data: dict):
        message = Message("create_chat", "client", "server", "_", Message.decode_content_to_json(data))
        await self.send_message(message)
