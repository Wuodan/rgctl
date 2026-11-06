from datetime import datetime

from app.schemas.common import ORMModel
from pydantic import BaseModel, EmailStr, Field


class UserResponse(ORMModel):
    id: str
    email: EmailStr
    name: str
    role: str
    created_at: datetime


class UserUpdateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
