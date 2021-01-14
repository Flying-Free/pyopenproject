from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class NewsCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/news"

    @abstractmethod
    def execute(self): raise NotImplementedError