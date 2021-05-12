from __future__ import annotations
import abc
from adapters import abstractRepository
from adapters import repository


class AbstractUnitOfWork(abc.ABC):
    model: abstractRepository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class EnergyUonitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.model = repository.EnergySourceRepo
        self.committed = False

    def __enter__(self):
        self.model = repository.EnergySourceRepo()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
