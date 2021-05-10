# import model
from domain.model import EnergySource
from pydantic.dict import Dict




class EnergySourceRepo:
    async def add(self,model:EnergySource):
        values={
            "name": model.name
            "address": model.address
            "energy_type": model.energy_type
            "email": model.email
            "avg_production": model.avg_production
            "payment_duration": model.payment_duration
            "payment_type": model.payment_type
        }
        await model.append(values)