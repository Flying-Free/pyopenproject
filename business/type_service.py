from abc import ABCMeta, abstractmethod


class TypeService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    # TODO: Review what params we need to create a new type
    @abstractmethod
    def new_type(self): raise NotImplementedError
