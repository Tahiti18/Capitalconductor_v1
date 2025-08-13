
from itsdangerous import URLSafeSerializer
from .config import settings

serializer = URLSafeSerializer(settings.JWT_SECRET)

def sign_invite(email: str, project_id: str) -> str:
    return serializer.dumps({"e": email, "p": project_id})

def verify_invite(token: str) -> dict|None:
    try:
        return serializer.loads(token)
    except Exception:
        return None
