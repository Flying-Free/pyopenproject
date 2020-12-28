from abc import ABCMeta, abstractmethod


class ProjectService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self, project): raise NotImplementedError

    @abstractmethod
    def update(self, project): raise NotImplementedError

    @abstractmethod
    def delete(self, project): raise NotImplementedError

    @abstractmethod
    def create(self, project): raise NotImplementedError

    @abstractmethod
    def create_form(self, project): raise NotImplementedError

    @abstractmethod
    def update_form(self, project): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters, sortBy): raise NotImplementedError

    @abstractmethod
    def find_parents(self, filters, of, sortBy): raise NotImplementedError

    # TODO: Review what params we need to create a new project
    # @abstractmethod
    # def new_project(self): raise NotImplementedError
