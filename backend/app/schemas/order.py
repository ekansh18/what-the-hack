from pydantic import BaseModel
from uuid import UUID
from datetime import date
from app.schemas.common import OrderStatus


class OrderlineBase(BaseModel):
    order_id: UUID
    sku: str
    quantity: int


class OrderlineCreate(OrderlineBase):
    pass


class Orderline(OrderlineBase):
    id: UUID

    model_config = {"from_attributes": True}


class OrderBase(BaseModel):
    customer_id: UUID
    creation_date: date
    delivery_id: UUID | None = None
    orderline_ids: list[UUID] = []
    recipes: list[UUID] = []
    status: OrderStatus = OrderStatus.paid
    total_price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: UUID

    model_config = {"from_attributes": True}
