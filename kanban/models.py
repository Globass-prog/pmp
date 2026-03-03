from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
    ]

    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")

    def __str__(self):
        return self.title