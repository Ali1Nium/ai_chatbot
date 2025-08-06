from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
from ninja.errors import HttpError
from ninja_extra import ControllerBase, api_controller, http_post

from chat.models.user_config_model import User
from chat.schema.user_config_schema import (
    LoginRequestSchema,
    RegisterRequest,
    RegisterResponse,
    TokenResponseSchema,
)


@api_controller("/v1/auth", tags=["Auth"])
class AuthController(ControllerBase):

    @http_post(
        "/register",
        response={200: RegisterResponse, 400: RegisterResponse},
    )
    async def register_user(self, request, payload: RegisterRequest):
        try:
            if await User.objects.filter(email=payload.email).aexists():
                return 400, RegisterResponse(success=False, message="User already exists")

            await User.objects.acreate(
                username=payload.email,
                email=payload.email,
                full_name=payload.full_name or "",
                password=make_password(payload.password),
            )

            return 200, RegisterResponse(success=True, message="User registered successfully")

        except Exception as e:
            return 400, RegisterResponse(success=False, message=f"Error: {str(e)}")

    @http_post(
        "/login",
        response={200: TokenResponseSchema, 401: None},
    )
    def login(self, data: LoginRequestSchema):
        user = authenticate(username=data.email, password=data.password)
        if not user:
            raise HttpError(401, "Invalid email or password")

        payload = {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(hours=24),
            "iat": datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        return 200, {
            "access": token,
            "refresh": "refresh_not_implemented",
        }
