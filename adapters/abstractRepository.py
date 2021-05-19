import abc
from domain import model
from typing import Set
class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen=set()

    def add(self,energy:model.EnergySource):
        self._add(energy)
        self.seen.add(energy)
        print("seen",self.seen)

    def get(self, id_) -> model.EnergySource:  #(3)
        energy = self._get(id_)
        if energy:
            self.seen.add(energy)
        return energy

    @abc.abstractmethod
    def _add(self, energy:model.EnergySource):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id_=None) -> model.EnergySource :
        raise NotImplementedError

    @abc.abstractmethod
    def update(self,id_=None, model=None):
        raise NotImplementedError
    