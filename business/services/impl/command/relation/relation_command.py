from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class RelationCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/relations"

    @abstractmethod
    def execute(self): raise NotImplementedError
