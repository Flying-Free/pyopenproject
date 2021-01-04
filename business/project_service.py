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
    def find_all(self, filters, sortBy): raise NotImplementedError

    @abstractmethod
    def create(self, project): raise NotImplementedError

    @abstractmethod
    def find_schema(self): raise NotImplementedError

    @abstractmethod
    def create_form(self, project): raise NotImplementedError

    @abstractmethod
    def update_form(self, project): raise NotImplementedError

    @abstractmethod
    def find_parents(self, filters, of, sortBy): raise NotImplementedError

    #Documentation in the page for the Version endpoint
    @abstractmethod
    def find_versions(self, project): raise NotImplementedError

    # Documentation in the page for the Type endpoint
    @abstractmethod
    def find_types(self, project): raise NotImplementedError

    # Documentation in the page for the Budget endpoint
    @abstractmethod
    def find_budgets(self, project): raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def find_work_packages(self, project): raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def create_work_package(self, project, notify, workPackage): raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def create_work_package_form(self, project, notify, form): raise NotImplementedError