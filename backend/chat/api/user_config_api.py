from chat.models.user_config_model import User
from chat.schema.user_config_schema import RegisterRequest, RegisterResponse
from ninja_extra import api_controller, http_post
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError

@api_controller("/v1/auth", tags=["Auth"])
class AuthController:

    @http_post(
        "/register",
        response={200: RegisterResponse, 400: RegisterResponse}
    )
    async def register_user(self, request, payload: RegisterRequest):
        try:
            if await User.objects.filter(email=payload.email).aexists():
                return 400, RegisterResponse(success=False, message="User already exists")

            user = await User.objects.acreate(
                username=payload.email,
                email=payload.email,
                full_name=payload.full_name or "",
                password=make_password(payload.password)
            )
            return RegisterResponse(success=True, message="User registered successfully")

        except Exception as e:
            return 400, RegisterResponse(success=False, message=f"Error: {str(e)}")
