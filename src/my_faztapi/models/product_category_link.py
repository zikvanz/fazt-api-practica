from sqlmodel import Field, SQLModel


class ProductCategoryLink(SQLModel, table=True):
    id_product: int = Field(default=None, foreign_key="product.id", primary_key=True)
    id_category: int = Field(default=None, foreign_key="category.id", primary_key=True)
