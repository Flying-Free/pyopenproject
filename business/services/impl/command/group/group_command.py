from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class GroupCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/groups"

    @abstractmethod
    def execute(self): raise NotImplementedError
