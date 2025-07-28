
from django.db import models

from chat.models.chat_history_model import ChatHistory


class FileReference(models.Model):
    chat = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, related_name="files")
    file_id = models.CharField(max_length=100)  # آیدی در MinIO یا سیستم فایل
    text_summary = models.TextField(blank=True, null=True)
    vector_path = models.CharField(max_length=255, blank=True, null=True)  # مسیر وکتورها اگه هست
    created_at = models.DateTimeField(auto_now_add=True)
