from typing import Optional

from ninja import Schema
from pydantic import EmailStr


class RegisterRequest(Schema):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class RegisterResponse(Schema):
    success: bool
    message: str


class LoginRequestSchema(Schema):
    email: EmailStr
    password: str


class TokenResponseSchema(Schema):
    access: str
    refresh: str
