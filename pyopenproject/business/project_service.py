from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class ProjectService(AbstractService):
    """
    Class ProjectService,
    service for project endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, project): raise NotImplementedError

    @abstractmethod
    def update(self, project): raise NotImplementedError

    @abstractmethod
    def delete(self, project): raise NotImplementedError

    @abstractmethod
    def find_all(self, filters=None, sort_by=None): raise NotImplementedError

    @abstractmethod
    def create(self, project): raise NotImplementedError

    @abstractmethod
    def find_schema(self): raise NotImplementedError

    @abstractmethod
    def create_form(self, form): raise NotImplementedError

    @abstractmethod
    def update_form(self, form): raise NotImplementedError

    @abstractmethod
    def find_parents(self, filters, of, sort_by): raise NotImplementedError

    # Documentation in the page for the Version endpoint
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
    def find_work_packages(self, project, offset, page_size, filters, group_by, sort_by, show_sums):
        raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def create_work_package(self, project, work_package, notify): raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def create_work_package_form(self, project, form): raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def find_available_assignees(self, project): raise NotImplementedError

    # Documentation in the page for the Work Package endpoint
    @abstractmethod
    def find_available_responsibles(self, project): raise NotImplementedError
