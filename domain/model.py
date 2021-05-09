from pydantic import BaseModel
from datetime import Optional, date, datetime
# from email import email
from enum import Enum


class PaymentType(str, Enum):
    monthly = "monthly"
    yearly = "yearly"


class EnergyType(BaseModel):
    name:
    created_date: str


class EnergySource(BaseModel):
    name: str
    address: str
    energy_type: EnergyType
    email: str
    avg_production: float
    payment_duration: int
    payment_type: PaymentType

    class Config:
        use_enum_values = True


class energysource_factory(
    name: str
    address: str
    energy_type: EnergyType
    email: str
    avg_production: float
    payment_duration: int
    payment_type: PaymentType
) -> EnergySource:
    return EnergySource(
        name=name,
        address=address,
        energy_type=energy_type,
        email=email,
        avg_production=avg_production,
        payment_duration=payment_duration,
        payment_type=payment_type
    )
