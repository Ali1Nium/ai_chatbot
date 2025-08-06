from asgiref.sync import sync_to_async
from ninja_extra import ControllerBase, api_controller, http_post

from chat.schema.text_chat_api import (
    TextChatRequestSchema,
    TextChatResponseSchema,
)
from config.OAUTH import PureAsyncJWTAuth


@api_controller("/v1/chat", tags=["Chat"], auth=PureAsyncJWTAuth())
class TextChatController(ControllerBase):

    @http_post(
        "/send-message",
        response={200: TextChatResponseSchema},
    )
    async def send_message(self, request, data: TextChatRequestSchema):
        user = request.user
        full_name = await sync_to_async(lambda: user.full_name)()
        text = data.message.strip()

        return TextChatResponseSchema(
            reply=f"{full_name} says: {text}"
        )
