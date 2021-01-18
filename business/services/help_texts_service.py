from abc import ABCMeta, abstractmethod


class HelpTextsService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, help_text): raise NotImplementedError

    @abstractmethod
    def find_all(self): raise NotImplementedError