from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class CategoryCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/categories/"

    @abstractmethod
    def execute(self): raise NotImplementedError
