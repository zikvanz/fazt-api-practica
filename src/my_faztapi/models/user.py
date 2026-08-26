from __future__ import annotations

from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship

from my_faztapi.schemas.user import UserBase

if TYPE_CHECKING:
    from my_faztapi.models.order import Order
    from my_faztapi.models.user_profile import UserProfile


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    orders: list["Order"] = Relationship(back_populates="user")
    profile: UserProfile | None = Relationship(
        back_populates="user", sa_relationship_kwargs={"uselist": False}
    )
