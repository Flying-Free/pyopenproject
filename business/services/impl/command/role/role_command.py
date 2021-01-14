from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class RoleCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/roles"

    @abstractmethod
    def execute(self): raise NotImplementedError
