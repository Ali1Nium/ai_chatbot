from django.db import models

from chat.models.user_config_model import User

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_histories")
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, related_name="messages")
    sender = models.CharField(max_length=20, default="user")
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
