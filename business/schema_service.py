from abc import ABCMeta, abstractmethod


class SchemaService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    # TODO: Review what params we need to create a new schema
    @abstractmethod
    def new_schema(self): raise NotImplementedError
