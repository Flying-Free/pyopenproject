from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class PriorityCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/priorities"

    @abstractmethod
    def execute(self): raise NotImplementedError
