import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from ninja.security import HttpBearer
from asgiref.sync import sync_to_async

User = get_user_model()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

class PureAsyncJWTAuth(HttpBearer):
    async def authenticate(self, request, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")
            if not user_id:
                return None

            user = await sync_to_async(User.objects.get)(id=user_id)
            return user

        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        except User.DoesNotExist:
            return None
