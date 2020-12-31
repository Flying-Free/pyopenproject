from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class VersionCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/versions"

    @abstractmethod
    def execute(self): raise NotImplementedError
