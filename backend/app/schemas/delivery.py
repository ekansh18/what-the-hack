from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DeliveryBase(BaseModel):
    timeslot: str             # e.g. "2026-04-08 10:00-12:00"
    delivery_moment: datetime | None = None
    trip_id: UUID | None = None
    hub_id: str
    fc_id: str


class DeliveryCreate(DeliveryBase):
    pass


class Delivery(DeliveryBase):
    id: UUID

    model_config = {"from_attributes": True}


class StockBase(BaseModel):
    sku: str
    fc_id: str
    stock_location: str
    quantity: int
    last_delivery_timestamp: datetime | None = None
    is_marked_imperfect: bool = False


class Stock(StockBase):
    model_config = {"from_attributes": True}


class FCBase(BaseModel):
    address: str
    country: str


class FC(FCBase):
    id: str

    model_config = {"from_attributes": True}


class HubBase(BaseModel):
    address: str
    country: str


class Hub(HubBase):
    id: str

    model_config = {"from_attributes": True}
