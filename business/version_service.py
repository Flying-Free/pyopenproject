from abc import ABCMeta, abstractmethod


class VersionService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, version): raise NotImplementedError

    @abstractmethod
    def update_version(self, version): raise NotImplementedError

    @abstractmethod
    def delete_version(self, version): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters): raise NotImplementedError

    @abstractmethod
    def new_version(self, version): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find_schema(self): raise NotImplementedError

    @abstractmethod
    def new_version_form(self, version): raise NotImplementedError

    @abstractmethod
    def update_version_form(self, version): raise NotImplementedError

    @abstractmethod
    def find_projects(self): raise NotImplementedError