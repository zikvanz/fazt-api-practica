from sqlmodel import Field

from my_faztapi.schemas.order import OrderOut
from my_faztapi.schemas.user import UserOut


class UserWithOrders(UserOut):
    orders: list[OrderOut] = Field(default_factory=list)
