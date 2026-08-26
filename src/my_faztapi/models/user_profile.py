from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from my_faztapi.models.user import User


class UserProfile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    bio: str
    avatar_url: str
    user_id: int = Field(foreign_key="user.id", unique=True)
    user: "User" = Relationship(back_populates="profile")
