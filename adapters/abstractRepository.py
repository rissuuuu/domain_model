import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model=None):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id=None):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self,id=None, model=None):
        raise NotImplementedError
    