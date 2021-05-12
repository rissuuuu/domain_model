import abc
class AbstractRepository(abc.ABC):
    @abc.abstractmethod  
    def add(self, model=None):
        raise NotImplementedError  