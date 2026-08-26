from sqlmodel import Field, Relationship, SQLModel

from my_faztapi.models.category import Category
from my_faztapi.models.product_category_link import ProductCategoryLink


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    categories: list["Category"] = Relationship(
        back_populates="products", link_model=ProductCategoryLink
    )
