from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from my_faztapi.schemas.order import OrderBase

if TYPE_CHECKING:
    from my_faztapi.models.user import User


class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="orders")
