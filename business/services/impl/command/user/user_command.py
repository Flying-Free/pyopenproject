from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class UserCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/users/"

    @abstractmethod
    def execute(self): raise NotImplementedError
