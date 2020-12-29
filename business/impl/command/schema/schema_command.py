from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class SchemaCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/schema"

    @abstractmethod
    def execute(self): raise NotImplementedError
