import abc
from domain.model import EnergySource
class AbstractRepository(abc.ABC):
    @abc.abstractmethod  
    def add(self, EnergySource):
        raise NotImplementedError  