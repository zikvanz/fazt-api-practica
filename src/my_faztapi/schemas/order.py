from sqlmodel import Field, SQLModel


class OrderBase(SQLModel):
    total: int = Field(gt=0)


class OrderCreate(OrderBase):
    user_id: int


class OrderOut(OrderBase):
    id: int


class OrderOutWithUserId(OrderOut):
    user_id: int
