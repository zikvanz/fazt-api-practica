from sqlmodel import Field, Relationship, SQLModel

from my_faztapi.models.product import Product
from my_faztapi.models.product_category_link import ProductCategoryLink


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    products: list["Product"] = Relationship(
        back_populates="categories", link_model=ProductCategoryLink
    )
