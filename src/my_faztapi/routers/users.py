from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from my_faztapi.database import get_session
from my_faztapi.models.user import User
from my_faztapi.schemas.user import UserCreate, UserOut
from my_faztapi.schemas.user_with_orders import UserWithOrders

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut)
def create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    user = User.model_validate(user_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/{user_id}", response_model=UserWithOrders)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No encontrado")
    return user
