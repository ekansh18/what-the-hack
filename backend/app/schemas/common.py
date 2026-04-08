from enum import Enum


class OrderStatus(str, Enum):
    paid = "paid"
    fulfilled = "fulfilled"
    in_transit = "in transit"
    delivered = "delivered"
