import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from apps.projects.models import Project
from apps.tasks.models import Task

class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            "dashboard_group",
            self.channel_name
        )
        await self.accept()
        await self.send_stats()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "dashboard_group",
            self.channel_name
        )

    async def send_stats(self):

        projects = await sync_to_async(Project.objects.count)()
        tasks = await sync_to_async(Task.objects.count)()
        done = await sync_to_async(Task.objects.filter(status="done").count)()

        data = {
            "projects": projects,
            "tasks": tasks,
            "done": done,
        }

        await self.send(text_data=json.dumps(data))

    async def dashboard_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))