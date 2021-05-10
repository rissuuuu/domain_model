from pydantic import BaseModel
from datetime import Optional, date, datetime
# from email import email
from enum import Enum


class PaymentType(str, Enum):
    monthly = "monthly"
    yearly = "yearly"


class AddEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: PaymentType

    class Config:
        use_enum_values = True

class EnergySourceAbstract(BaseModel):
    energy_source:EnergySource