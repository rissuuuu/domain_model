from __future__ import annotations
import abc
from adapters import abstractRepository
from adapters import repository
from domain.model import EnergySource

class AbstractUnitOfWork(abc.ABC):
    repo: repository.AbstractRepository 

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
    def commit(self): 
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

    def commit(self):
        self.repo.add(self.data_to_store)

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

    def commit(self):
        self.repo.update(self.id_,self.data_to_update)

    def rollback(self):
        pass