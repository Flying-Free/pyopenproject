from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class WikiPageCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/wiki_pages"

    @abstractmethod
    def execute(self): raise NotImplementedError
