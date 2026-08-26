from pydantic import EmailStr
from sqlmodel import SQLModel


class UserBase(SQLModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
