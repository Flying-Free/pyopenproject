from abc import ABCMeta, abstractmethod


class RenderService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_markdown(self, context): raise NotImplementedError

    @abstractmethod
    def to_plain(self, context): raise NotImplementedError
