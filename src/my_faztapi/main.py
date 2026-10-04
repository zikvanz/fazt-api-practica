from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from my_faztapi.database import create_db_and_tables
from my_faztapi.routers import items, orders, products, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(items.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(orders.router)


# Crea GET / que devuelva {"message": "Bienvenido a mi API"}.
# Crea GET /version que devuelva {"version": "1.0.0"}.
# Abre /docs (Swagger UI) y prueba ambos endpoints desde ahí.
@app.get("/")
def get_root():
    return {"message": "Bienvenido a mi API"}


@app.get("/version")
def get_version():
    return {"version": "1.0.0"}


# GET    /products         → get_products()
# GET    /products/{id}    → get_product()
# POST   /products         → create_product()
# PUT    /products/{id}    → update_product()
# PATCH  /products/{id}    → patch_product()
# DELETE /products/{id}    → delete_product()

# Crea GET /users/{user_id}/orders/{order_id} que devuelva ambos IDs.
# Crea GET /search con query params q: str (obligatorio) y page: int = 1.
# ¿Qué pasa si llamas /search sin q? Explica el error que ves en /docs.


@app.get("/search")
def get_users(q: str, page: int = 1):
    return {"q": q, "page": page}


# Crea DELETE /products/{product_id} que devuelva 404 si no existe, o {"deleted": True} si sí.
# Crea POST /login que reciba username y password, y devuelva 401 con detail="Credenciales inválidas" si no coinciden con valores fijos.


class LoginRequest(BaseModel):
    username: str
    password: str


db_users = [{"id": 1, "username": "jean", "password": "holi"}]


@app.post("/login")
def login(user: LoginRequest):
    user_bd = next(
        (u for u in db_users if u["username"] == user.username),
        None,
    )
    if user_bd == None:
        raise HTTPException(status_code=401, detail="credenciales invalidas u")
    if user_bd["password"] != user.password:
        raise HTTPException(status_code=401, detail="credenciales invalidas p")
    return {"message": "loguin existoso"}
