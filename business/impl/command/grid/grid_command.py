from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class GridCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/grids"

    @abstractmethod
    def execute(self): raise NotImplementedError
