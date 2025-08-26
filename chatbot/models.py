from django.db import models
from users.models import User

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[("user","User"), ("assistant","Assistant")])
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
