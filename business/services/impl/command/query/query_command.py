from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class QueryCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/queries"

    @abstractmethod
    def execute(self): raise NotImplementedError
