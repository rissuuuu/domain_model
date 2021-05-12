from adapters.abstractRepository import AbstractRepository
from domain.model import EnergySource


class EnergySourceRepo(AbstractRepository):
    def add(self, model: EnergySource):
        values = {
            "name": model.name,
            "address": model.address,
            "energy_type": model.energy_type,
            "email": model.email,
            "avg_production": model.avg_production,
            "payment_duration": model.payment_duration,
            "payment_type": model.payment_type
        }
        with open("file.json", "a+") as f:
            f.write(f'{values}\n')
