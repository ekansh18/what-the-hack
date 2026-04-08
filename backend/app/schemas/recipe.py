# from pydantic import BaseModel
# from uuid import UUID
# from datetime import timedelta


# class RecipeBase(BaseModel):
#     name: str
#     description: str | None = None
#     quantified_ingredients: dict[UUID, int]   # ingredient_id → quantity
#     portion_quantity: int
#     cook_time: timedelta | None = None
#     instructions: list[str]


# class RecipeCreate(RecipeBase):
#     pass


# class Recipe(RecipeBase):
#     id: UUID

#     model_config = {"from_attributes": True}
from pydantic import BaseModel


class Recipe(BaseModel):
    name: str
    quantity: int
    ingredients: list[str]
