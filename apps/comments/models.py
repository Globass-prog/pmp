from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from apps.tasks.models import Task


class Comment(models.Model):

    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user}"