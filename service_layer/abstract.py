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



class EnergySourceAbstract(BaseModel):
    energy_source:EnergySource

class UpdateEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: str
