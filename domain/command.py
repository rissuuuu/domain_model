from pydantic import BaseModel
from domain.model import EnergySource


class AddEnergySource(BaseModel):
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: str


class EnergySourceCommand(BaseModel):
    energy_source: EnergySource

class UpdateEnergySource(EnergySourceCommand):
    print("Command")
    name: str
    address: str
    energy_type: str
    email: str
    avg_production: float
    payment_duration: int
    payment_type: str

class UpdateEnergyName(EnergySourceCommand):
    name:str

class UpdateEnergyAddress(EnergySourceCommand):
    address: str

class UpdateEnergyType(EnergySourceCommand):
    energy_type: str

class UpdateEnergyEmail(EnergySourceCommand):
    email: str

class UpdateEnergyProd(EnergySourceCommand):
    avg_production: float

class UpdateEnergyPayDur(EnergySourceCommand):
    payment_duration: int

class UpdateEnergyPayTyp(EnergySourceCommand):
    payment_type: str
