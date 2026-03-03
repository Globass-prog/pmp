from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apps.projects.models import Project
from apps.tasks.models import Task
import json

@receiver(post_save, sender=Task)
def update_dashboard(sender, instance, **kwargs):

    channel_layer = get_channel_layer()

    projects = instance.project.__class__.objects.count()
    tasks = Task.objects.count()
    done = Task.objects.filter(status="done").count()

    data = {
        "projects": projects,
        "tasks": tasks,
        "done": done,
    }

    async_to_sync(channel_layer.group_send)(
        "dashboard_group",
        {
            "type": "dashboard_update",
            "data": data
        }
    )