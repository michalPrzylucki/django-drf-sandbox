from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Task(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
