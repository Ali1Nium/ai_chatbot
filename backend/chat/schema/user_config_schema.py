from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterRequest(BaseModel):
    email: EmailStr
    # email: str
    password: str
    full_name: Optional[str] = None

class RegisterResponse(BaseModel):
    success: bool
    message: str
