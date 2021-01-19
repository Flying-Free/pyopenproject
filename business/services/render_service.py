from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class RenderService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def to_markdown(self, text): raise NotImplementedError

    @abstractmethod
    def to_markdown_by_context(self, context, text): raise NotImplementedError

    @abstractmethod
    def to_plain(self, context): raise NotImplementedError
