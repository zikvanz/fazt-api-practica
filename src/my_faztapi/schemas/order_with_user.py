from my_faztapi.schemas.order import OrderOut
from my_faztapi.schemas.user import UserOut


class OrderWithUser(OrderOut):
    user: UserOut
