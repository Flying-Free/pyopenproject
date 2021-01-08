from abc import ABCMeta, abstractmethod


class AttachmentService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, attachment): raise NotImplementedError

    @abstractmethod
    def delete(self, attachment): raise NotImplementedError

    @abstractmethod
    def find(self, attachment): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def download_by_context(self,context): raise NotImplementedError
