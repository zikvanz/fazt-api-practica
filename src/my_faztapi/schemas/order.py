from sqlmodel import SQLModel


class OrderBase(SQLModel):
    total: int


class OrderCreate(OrderBase):
    user_id: int


class OrderOut(OrderBase):
    id: int


class OrderOutWithUserId(OrderOut):
    user_id: int
