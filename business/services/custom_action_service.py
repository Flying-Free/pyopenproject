from abc import ABCMeta, abstractmethod


class CustomActionService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, custom_action): raise NotImplementedError

    @abstractmethod
    def execute(self, custom_action): raise NotImplementedError
