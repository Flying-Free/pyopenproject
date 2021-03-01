from abc import abstractmethod, ABCMeta

from pyopenproject.business.services.command.command import Command


class ConfigurationCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/configuration"

    def __init__(self, connection):
        """Constructor for class ConfigurationCommand, from Command.

        :param connection: The connection data
        """
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
