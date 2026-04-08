# from pydantic import BaseModel
# from uuid import UUID


# class ArticleBase(BaseModel):
#     name: str
#     sku: str
#     category: str
#     nutrition_table: str | None = None
#     nutriscore: str | None = None
#     carbon_footprint: float | None = None
#     is_biological: bool = False
#     description: str | None = None
#     allergy_labels: list[str] = []
#     image_url: str | None = None
#     is_available: bool = True
#     price: float


# class ArticleCreate(ArticleBase):
#     pass


# class Article(ArticleBase):
#     id: UUID

#     model_config = {"from_attributes": True}

from pydantic import BaseModel


class Article(BaseModel):
    name: str
    price: float
    nutri_score: str  # Using nutri_score as per your request
