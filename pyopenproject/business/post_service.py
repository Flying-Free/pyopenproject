from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class PostService(AbstractService):
    """
    Class PostService,
    service for post endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def list_attachments(self, post): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, post, attachment, file_path): raise NotImplementedError

    @abstractmethod
    def find(self, post): raise NotImplementedError
