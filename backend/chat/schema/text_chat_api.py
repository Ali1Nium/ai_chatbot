from ninja import Schema
from typing import Optional

class TextChatRequestSchema(Schema):
    message: str

class TextChatResponseSchema(Schema):
    reply: str
