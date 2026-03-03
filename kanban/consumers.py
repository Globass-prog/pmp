import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AdminDashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "Connected"
        }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass