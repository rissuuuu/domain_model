from pydantic import BaseModel
# from datetime import Optional, date, datetime
# from email import email
from domain.model import EnergySource
from enum import Enum

class AddEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: str


class UpdateEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str =None
    avg_production: float =None
    payment_duration: int =None
    payment_type: str
