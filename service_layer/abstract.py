from pydantic import BaseModel
# from datetime import Optional, date, datetime
# from email import email
from domain.model import EnergySource
from enum import Enum
from typing import Optional

class AddEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: str


class UpdateEnergySource(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    energy_type: Optional[str] = None
    email: Optional[str] = None
    avg_production: Optional[float] = None
    payment_duration: Optional[int] = None
    payment_type: Optional[str] = None
