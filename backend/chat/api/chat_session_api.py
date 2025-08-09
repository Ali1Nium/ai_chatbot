from chat.models.chat_history_model import ChatHistory
from ninja_extra import api_controller, ControllerBase, http_post
from asgiref.sync import sync_to_async
from chat.models.user_config_model import User
from config.OAUTH import PureAsyncJWTAuth

@api_controller("/v1/chat", tags=["Chat"], auth=PureAsyncJWTAuth())
class ChatManagementController(ControllerBase):

    @http_post("/start-or-get-chat")
    async def start_or_get_chat(self, request):
        user = request.user 

        chat = await sync_to_async(
            lambda: ChatHistory.objects.filter(user=user).order_by("-created_at").first()
        )()

        if not chat:
            chat = await sync_to_async(ChatHistory.objects.create)(user=user)

        return {"chat_id": chat.id}
