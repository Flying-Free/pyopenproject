from abc import abstractmethod, ABCMeta

from pyopenproject.business.services.command.command import Command


class WikiPageCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/wiki_pages"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
