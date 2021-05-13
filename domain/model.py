from pydantic import BaseModel
# from email import email
from enum import Enum
from typing import Dict,Any


class EnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: str

    class Config:
        allow_mutation = True
    
    def update(self,mapping:Dict[str,Any]):
        return self.copy(update=mapping)


def energysource_factory(
    name: str,
    address: str,
    energy_type: str,
    email: str,
    avg_production: float,
    payment_duration: int,
    payment_type: str,
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
