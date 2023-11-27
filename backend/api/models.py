import datetime
import uuid
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Describes a task
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.datetime.utcnow)