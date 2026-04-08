from pydantic import BaseModel, EmailStr
from datetime import date
from uuid import UUID


class CustomerBase(BaseModel):
    name: str
    date_of_birth: date
    email: str
    phone_number: str
    address: str
    country: str
    house_hold_size: int


class CustomerCreate(CustomerBase):
    pass                          # what you receive when creating


class Customer(CustomerBase):
    id: UUID                      # what you return — includes the ID

    model_config = {"from_attributes": True}
