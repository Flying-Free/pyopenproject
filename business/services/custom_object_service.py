from abc import ABCMeta, abstractmethod


class CustomObjectService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, custom_object): raise NotImplementedError
