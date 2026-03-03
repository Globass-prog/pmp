from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from apps.projects.models import Project


class Task(models.Model):

    STATUS_CHOICES = (
        ('BACKLOG', 'Backlog'),
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('TESTING', 'Testing'),
        ('DONE', 'Done'),
    )

    PRIORITY_CHOICES = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='BACKLOG')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='MEDIUM')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title