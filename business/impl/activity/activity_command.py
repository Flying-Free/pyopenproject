from abc import abstractmethod, ABCMeta
from src.extract.business.impl.command import Command


class ActivityCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/activities"

    @abstractmethod
    def execute(self): raise NotImplementedError
