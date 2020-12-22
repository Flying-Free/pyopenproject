from abc import abstractmethod, ABCMeta
from business.impl.command import Command


class WorkPackageCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/work_packages/"

    @abstractmethod
    def execute(self): raise NotImplementedError
