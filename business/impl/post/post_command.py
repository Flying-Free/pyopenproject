from abc import abstractmethod, ABCMeta
from business.impl.command import Command


class PostCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/posts"

    @abstractmethod
    def execute(self): raise NotImplementedError
