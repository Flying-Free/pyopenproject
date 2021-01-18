from abc import ABCMeta, abstractmethod


class WikiPageService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, wiki_page): raise NotImplementedError

    @abstractmethod
    def find_attachments(self, context, identifier, body): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, context, identifier, body): raise NotImplementedError
