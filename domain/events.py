from dataclasses import dataclass

class Event:
    pass
    

@dataclass
class EnergySourceCreated(Event):
    energy_id: str
