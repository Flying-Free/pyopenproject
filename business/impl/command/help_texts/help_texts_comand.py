from abc import abstractmethod, ABCMeta

from business.impl.command.command import Command


class HelpTextsCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/help_texts"

    @abstractmethod
    def execute(self): raise NotImplementedError