from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class PrincipalCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/principals"

    @abstractmethod
    def execute(self): raise NotImplementedError
