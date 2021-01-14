from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class DocumentCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/documents"

    @abstractmethod
    def execute(self): raise NotImplementedError
