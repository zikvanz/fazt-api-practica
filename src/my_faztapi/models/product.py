from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from my_faztapi.models.product_category_link import ProductCategoryLink

if TYPE_CHECKING:
    from my_faztapi.models.category import Category


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    categories: list["Category"] = Relationship(
        back_populates="products", link_model=ProductCategoryLink
    )
