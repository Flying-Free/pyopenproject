from abc import ABCMeta, abstractmethod


class PostService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list_attachments(self, post): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, post, attachment): raise NotImplementedError

    @abstractmethod
    def find(self, post): raise NotImplementedError
