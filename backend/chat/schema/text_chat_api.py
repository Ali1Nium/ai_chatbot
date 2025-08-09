from ninja import Schema
from typing import Optional

class TextChatRequestSchema(Schema):
    message: str
    userChatId: str

class TextChatResponseSchema(Schema):
    aiResponse: str
    userChatId: str
