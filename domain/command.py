from pydantic import BaseModel
from datetime import date
from domain.model import EnergyType, EnergySource


class AddEnergyType(BaseModel):
    name: str
    created_date: str


class EnergyTypeCommand(BaseModel):
    energy_type = EnergyType


class AddEnergySource(BaseModel):
    name: str
    address: str
    energy_type: EnergyType
    email: str
    avg_production: float
    payment_duration: int
    payment_type: PaymentType

class EnergySourceCommand(BaseModel):
    energy_source = EnergySource