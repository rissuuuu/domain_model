import os
import pickle
from adapters.abstractRepository import AbstractRepository
from domain.model import EnergySource
from datetime import datetime
database={}
i=0
class EnergySourceRepo(AbstractRepository):
    def get(self,id:int) -> EnergySource:
        data=database[id]
        print("GET,data",data)
        energydata=EnergySource(**data)
        return energydata

    def add(self, model: EnergySource) -> None:
        values = {
            "name": model.name,
            "address": model.address,
            "energy_type": model.energy_type,
            "email": model.email,
            "avg_production": model.avg_production,
            "payment_duration": model.payment_duration,
            "payment_type": model.payment_type
        }
        global i
        i+=1
        database[i]=values
        with open('database.pickle', 'wb') as handle:
            pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print(database)

    def update(self,id,model: EnergySource) -> None:
        values = {
            "name": model.name,
            "address": model.address,
            "energy_type": model.energy_type,
            "email": model.email,
            "avg_production": model.avg_production,
            "payment_duration": model.payment_duration,
            "payment_type": model.payment_type
        }
        database[id]=values
        print(database)