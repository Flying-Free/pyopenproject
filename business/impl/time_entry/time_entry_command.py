from abc import abstractmethod, ABCMeta
from src.extract.business.impl.command import Command


class TimeEntryCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/time_entries"

    @abstractmethod
    def execute(self): raise NotImplementedError
