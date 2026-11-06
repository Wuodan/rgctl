from app.utils.dependencies import AuthUser, get_auth_user
from fastapi import Header


def require_auth(authorization: str | None = Header(default=None)) -> AuthUser:
    return get_auth_user(authorization)
