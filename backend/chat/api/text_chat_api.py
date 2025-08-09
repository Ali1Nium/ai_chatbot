from asgiref.sync import sync_to_async
from chat.services.llm.clinet import call_llm
from chat.services.history_service import get_chat_history_for_model, save_user_and_assistant_messages
from chat.services.llm.message_builder import build_llm_messages
from ninja_extra import ControllerBase, api_controller, http_post
import logging
from chat.schema.text_chat_api import (
    TextChatRequestSchema,
    TextChatResponseSchema,
)
from config.OAUTH import PureAsyncJWTAuth

logger = logging.getLogger("===Text Chat API===")

@api_controller("/v1/chat", tags=["Chat"], auth=PureAsyncJWTAuth())
class TextChatController(ControllerBase):

    @http_post("/send-message", response={200: TextChatResponseSchema})
    async def send_message(self, request, payload: TextChatRequestSchema):
        user_message = payload.message
        user_chat_id = payload.userChatId
        user = request.user
        full_name = await sync_to_async(lambda: user.full_name)()

        history = await get_chat_history_for_model(user_chat_id)

        llm_input = await build_llm_messages(
            prompt_system="Your system prompt here",
            user_input=user_message,
            chat_history=history
        )

        ai_response = await call_llm(messages=llm_input)

        await save_user_and_assistant_messages(
            chat_id=user_chat_id,
            user_text=user_message,
            assistant_text=ai_response
        )
        return TextChatResponseSchema(
            aiResponse=ai_response,
            userChatId=user_chat_id
        )
