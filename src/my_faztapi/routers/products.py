from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, select

from my_faztapi.database import get_session
from my_faztapi.models.product import Product

router = APIRouter(prefix="/products", tags=["products"])


# Crea un modelo ProductCreate con name: str, price: float (mayor a 0), in_stock: bool = True.
# Crea POST /products que reciba ese modelo y lo devuelva tal cual.
# Prueba mandar price: -5 desde /docs y observa el error.

# Agrega un modelo ProductOut sin un campo cost_internal (costo interno) y úsalo como response_model.
# Investiga qué hace model_config = {"from_attributes": True} en Pydantic (te servirá con bases de datos).


# class ProductCreate(BaseModel):
#     name: str
#     price: float = Field(gt=0)
#     in_stock: bool = True
#     cost_internal: float


# class ProductOut(BaseModel):
#     name: str
#     price: float = Field(gt=0)
#     in_stock: bool = True


# @router.post("")
# def create_product(product: ProductCreate):
#     return {"message": f"producto creado {product}"}


# db_fake = [{"id": 1, "name": "torta"}, {"id": 2, "name": "leche"}]


# @router.delete("/{product_id}")
# def delete_product(product_id: int):
#     product = next(
#         (product for product in db_fake if product_id == product["id"]), None
#     )
#     if product == None:
#         raise HTTPException(status_code=404, detail="producto no encontrado")
#     db_fake.remove(product)
#     return {"deleted": f"se elimino {product}"}


# Agrega PUT /products/{product_id} y DELETE /products/{product_id} siguiendo el mismo patrón.
# Agrega un modelo User y una relación Order que pertenezca a un User (investiga Relationship de SQLModel).

class ProductBase(SQLModel):
    name: str
    price: float = Field(gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(SQLModel):
    name: str | None = None
    price: float | None = Field(default=None, gt=0)



@router.post("", response_model=Product)
def create_product(
    product_data: ProductCreate, session: Session = Depends(get_session)
):
    product = Product.model_validate(product_data)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@router.get("", response_model=list[Product])
def get_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="No encontrado")
    return product


@router.patch("/{product_id}", response_model=Product)
def patch_product(
    product_id: int,
    product_data: ProductUpdate,
    session: Session = Depends(get_session),
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="No encontrado")
    product.sqlmodel_update(product_data.model_dump(exclude_unset=True))
    session.commit()
    session.refresh(product)
    return product


@router.delete("/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(product)
    session.commit()
    return {"message": "producto eliminado"}
