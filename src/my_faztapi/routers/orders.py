# Crea una dependencia pagination_params(skip: int = 0, limit: int = 10) y úsala en dos endpoints distintos vía Depends.
# Crea una dependencia que simule "conexión a base de datos" (print("conectando...") y return {"db": "fake_connection"}), y úsala en un endpoint.

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from my_faztapi.database import get_session
from my_faztapi.models.order import Order
from my_faztapi.models.user import User
from my_faztapi.schemas.order import OrderCreate, OrderOutWithUserId


router = APIRouter(prefix="/orders", tags=["orders"])


def pagination_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


def connect_db():
    print("conectando...")
    return {"db": "conexion exitosa"}


@router.get("/list_orders_1")
def list_orders_1(pagination=Depends(pagination_params), db=Depends(connect_db)):
    print(db)
    return pagination


@router.get("/list_orders_2")
def list_orders_2(pagination=Depends(pagination_params)):
    return pagination


@router.post("", response_model=OrderOutWithUserId)
def create_order(order_data: OrderCreate, session: Session = Depends(get_session)):
    user = session.get(User, order_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    order = Order.model_validate(order_data)
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@router.get("/{order_id}", response_model=OrderOutWithUserId)
def get_order(order_id: int, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="No encontrado")
    return order
