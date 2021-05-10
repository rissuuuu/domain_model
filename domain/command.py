from pydantic import BaseModel
from datetime import date
from domain.model import EnergySource



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
