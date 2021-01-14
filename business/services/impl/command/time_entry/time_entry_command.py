from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class TimeEntryCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/time_entries"

    @abstractmethod
    def execute(self): raise NotImplementedError
