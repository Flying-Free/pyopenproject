from abc import ABCMeta, abstractmethod


class VersionService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    # TODO: Review what params we need to create a new version
    @abstractmethod
    def new_version(self): raise NotImplementedError
