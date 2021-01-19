from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class PostService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def list_attachments(self, post): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, post, attachment): raise NotImplementedError

    @abstractmethod
    def find(self, post): raise NotImplementedError
