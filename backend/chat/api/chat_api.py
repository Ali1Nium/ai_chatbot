from ninja_extra import api_controller, route
from ninja_extra.controllers import ControllerBase


@api_controller("/chat", tags=["Chat"])
class ChatController(ControllerBase):

    @route.get("/ping")
    def ping(self, request):
        return {"message": "pong"}
