from abc import abstractmethod, ABCMeta

from pyopenproject.business.services.command.command import Command


class CustomObjectCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/custom_objects"

    def __init__(self, connection):
        """Constructor for class CustomObjectCommand, from Command.

        :param connection: The connection data
        """
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
