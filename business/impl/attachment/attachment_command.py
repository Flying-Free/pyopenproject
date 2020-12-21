from abc import abstractmethod, ABCMeta
from src.extract.business.impl.command import Command


class AttachmentCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/attachment"

    @abstractmethod
    def execute(self): raise NotImplementedError
