from abc import ABCMeta, abstractmethod


class GroupService:
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find(self, group): raise NotImplementedError