from django.db import models
from django.contrib.auth.models import User
import uuid

class Conversation(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("resolved", "Resolved"),
    )

    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)

   
    intent = models.CharField(max_length=50, default="general")

   
    session_id = models.UUIDField(default=uuid.uuid4, editable=False)

    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.user.username} - {self.intent} - {self.status}"
