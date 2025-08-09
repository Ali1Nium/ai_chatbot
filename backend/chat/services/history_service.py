from typing import List, Dict
from chat.models.chat_history_model import ChatHistory, Message
from asgiref.sync import sync_to_async



async def get_chat_history_for_model(chat_id: int) -> List[Dict[str, str]]:
    
    messages = await sync_to_async(list)(
        Message.objects.filter(chat_id=chat_id)
        .order_by("created_at")
        .values("sender", "text")
    )
    
    role_map = {
        "user": "user",
        "assistant": "assistant",
        "system": "system"
    }
    
    formatted_messages = [
        {
            "role": role_map.get(msg["sender"], "user"),
            "content": msg["text"] or ""
        }
        for msg in messages
    ]
    
    return formatted_messages


async def save_user_and_assistant_messages(
    chat_id: int,
    user_text: str,
    assistant_text: str,
):
    chat = await sync_to_async(ChatHistory.objects.get)(id=chat_id)
    
    await sync_to_async(Message.objects.create)(
        chat=chat,
        sender="user",
        text=user_text,
    )
    
    await sync_to_async(Message.objects.create)(
        chat=chat,
        sender="assistant",
        text=assistant_text,
    )
