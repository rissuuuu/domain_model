from __future__ import annotations
import abc
from adapters import abstractRepository
from adapters import repository
from domain.model import EnergySource
from service_layer import messagebus
from domain import events

class AbstractUnitOfWork(abc.ABC):
    repo: repository.AbstractRepository 

    def commit(self):
        self._commit()
        self.publish_events()

    @abc.abstractmethod
    def publish_events(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __exit__(self, *args):
        self.rollback() 

    @abc.abstractmethod
    def _commit(self): 
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):  
        raise NotImplementedError


class EnergyUonitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = repository.EnergySourceRepo()

    def __enter__(self):
        self.data_to_store=None
        return self

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        self.repo.add(self.data_to_store)
    
    def publish_events(self):
        messagebus.handle(events.EnergySourceCreated(energy_id="a"))  #Just a check

    def rollback(self):
        pass

class UpdateEnergyUonitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = repository.EnergySourceRepo()

    def __enter__(self):
        self.id_=None
        self.data_to_update=None
        return self

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        self.repo.update(self.id_,self.data_to_update)
    
    def publish_events(self):
        messagebus.handle(events.EnergySourceUpdated(energy_id="a"))  #Just a check .

    def rollback(self):
        pass