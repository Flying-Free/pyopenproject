from abc import ABCMeta, abstractmethod


class CustomObjectService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, custom_object): raise NotImplementedError
