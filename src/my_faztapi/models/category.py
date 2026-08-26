from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from my_faztapi.models.product_category_link import ProductCategoryLink

if TYPE_CHECKING:
    from my_faztapi.models.product import Product


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    products: list["Product"] = Relationship(
        back_populates="categories", link_model=ProductCategoryLink
    )
