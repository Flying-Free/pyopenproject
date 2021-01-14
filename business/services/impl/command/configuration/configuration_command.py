from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class ConfigurationCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/configuration"

    @abstractmethod
    def execute(self): raise NotImplementedError
