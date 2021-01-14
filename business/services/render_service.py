from abc import ABCMeta, abstractmethod


class RenderService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_markdown(self, text): raise NotImplementedError

    @abstractmethod
    def to_markdown_by_context(self, context, text): raise NotImplementedError

    @abstractmethod
    def to_plain(self, context): raise NotImplementedError
