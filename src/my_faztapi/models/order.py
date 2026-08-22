from sqlmodel import Field, Relationship

from my_faztapi.models.user import User
from my_faztapi.schemas.order import OrderBase


class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="orders")
