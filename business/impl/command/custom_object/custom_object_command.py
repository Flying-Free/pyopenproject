from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class CustomObjectCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/custom_objects"

    @abstractmethod
    def execute(self): raise NotImplementedError
