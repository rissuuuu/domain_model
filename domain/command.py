from pydantic import BaseModel
from domain.model import EnergySource, PaymentType


class AddEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: PaymentType


class EnergySourceCommand(BaseModel):
    energy_source: EnergySource
