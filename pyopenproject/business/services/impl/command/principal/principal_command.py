from abc import abstractmethod, ABCMeta

from pyopenproject.business.services.impl.command import Command


class PrincipalCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/principals"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError