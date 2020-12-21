from abc import abstractmethod, ABCMeta
from src.extract.business.impl.command import Command


class ProjectCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/projects"

    @abstractmethod
    def execute(self): raise NotImplementedError
