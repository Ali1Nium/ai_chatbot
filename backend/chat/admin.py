from django.contrib import admin

from chat.models.chat_history_model import ChatHistory, Message
from chat.models.document_model import FileReference
from chat.models.user_config_model import User

# Register your models here.



admin.site.register(User)
admin.site.register(ChatHistory)
admin.site.register(Message)
admin.site.register(FileReference)

