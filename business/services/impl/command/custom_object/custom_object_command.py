from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class CustomObjectCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/custom_objects"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
