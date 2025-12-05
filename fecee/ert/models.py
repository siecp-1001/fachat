from django.db import models
from django.contrib.auth.models import User
import uuid

class Conversation(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("resolved", "Resolved"),
    )

    # Link to the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Track message and bot reply
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)

    # Optional: AI intent classification
    intent = models.CharField(max_length=50, default="general")

    # Session ID for multiple conversations
    session_id = models.UUIDField(default=uuid.uuid4, editable=False)

    # Status of conversation
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    # Timestamp
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.user.username} - {self.intent} - {self.status}"
