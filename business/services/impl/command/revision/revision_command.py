from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class RevisionCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/revisions"

    @abstractmethod
    def execute(self): raise NotImplementedError
