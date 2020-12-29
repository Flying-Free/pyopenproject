from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class RootCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3"

    @abstractmethod
    def execute(self): raise NotImplementedError
