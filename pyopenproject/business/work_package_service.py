from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class WorkPackageService(AbstractService):
    """
    Class WorkPackageService,
    service for work package endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find_attachments(self, work_package): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, work_package, attachment): raise NotImplementedError

    @abstractmethod
    def find(self, work_package): raise NotImplementedError

    @abstractmethod
    def update(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def delete(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_schema(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_all_schemas(self, filters): raise NotImplementedError

    @abstractmethod
    def update_form(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, page_size, filters, sort_by, group_by, show_sums): raise NotImplementedError

    @abstractmethod
    def create(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def create_form(self): raise NotImplementedError

    @abstractmethod
    def create_relation(self, relation_type, work_package_from, work_package_to, description): raise NotImplementedError

    @abstractmethod
    def find_relations(self, work_package): raise NotImplementedError

    @abstractmethod
    def create_relation_form(self, work_package, relation): raise NotImplementedError

    @abstractmethod
    def find_watchers(self, work_package): raise NotImplementedError

    @abstractmethod
    def create_watcher(self, work_package, user): raise NotImplementedError

    @abstractmethod
    def delete_watcher(self, work_package, watcher): raise NotImplementedError

    @abstractmethod
    def find_relation_candidates(self,
                                 work_package,
                                 query,
                                 filters=None,
                                 relation_type=None,
                                 page_size=None): raise NotImplementedError

    @abstractmethod
    def find_available_watchers(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_available_projects(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_revisions(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_activities(self, work_package): raise NotImplementedError

    @abstractmethod
    def create_activity(self, work_package, comment, notify): raise NotImplementedError
