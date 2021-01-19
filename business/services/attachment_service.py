from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class AttachmentService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def create(self, filename, description, file_path): raise NotImplementedError

    @abstractmethod
    def delete(self, attachment): raise NotImplementedError

    @abstractmethod
    def find(self, attachment): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def download_by_context(self,context): raise NotImplementedError
