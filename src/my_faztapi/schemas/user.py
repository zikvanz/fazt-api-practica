from sqlmodel import SQLModel


class UserBase(SQLModel):
    name: str


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
