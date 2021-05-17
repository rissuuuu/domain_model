from dataclasses import dataclass

class Event:
    pass
    

@dataclass
class EnergyNotGenerated(Event):
    energy_id: str
    class Config:
        arbitrary_types_allowed = True