from abc import ABCMeta, abstractmethod


class HelpTextsService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, help_text): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError