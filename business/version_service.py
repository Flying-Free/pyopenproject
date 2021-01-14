from abc import ABCMeta, abstractmethod


class VersionService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, version): raise NotImplementedError

    @abstractmethod
    def update(self, version): raise NotImplementedError

    @abstractmethod
    def delete(self, version): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError

    @abstractmethod
    def create(self, version): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find_schema(self): raise NotImplementedError

    @abstractmethod
    def create_form(self, version): raise NotImplementedError

    @abstractmethod
    def update_form(self, version): raise NotImplementedError

    @abstractmethod
    def find_projects(self): raise NotImplementedError