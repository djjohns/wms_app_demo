from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Task(models.Model):
    task_todo = models.CharField(
        help_text="Enter the task you want to accomplish.",
        max_length=255,
        validators=[MinLengthValidator(3, "Come on at least use a acronym!")],
    )
    task_dependencies = models.CharField(
        help_text="Enter what dependencies if any this task has.",
        max_length=255,
        validators=[MinLengthValidator(3, "Come on at least use a acronym!")],
    )
    task_accomplished = models.BooleanField(default=False,)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.task_todo
