from abc import ABCMeta, abstractmethod


class WorkPackageService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find_attachments(self, work_package): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, work_package, attachment): raise NotImplementedError

    @abstractmethod
    def find(self, notify): raise NotImplementedError

    @abstractmethod
    def update(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def delete_work_package(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def find_schema(self, schema): raise NotImplementedError

    @abstractmethod
    def find_all_schemas(self, filters): raise NotImplementedError

    @abstractmethod
    def update_form(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_all(self, notify, offset, pageSize,filters, sortBy, groupBy, showSums): raise NotImplementedError

    @abstractmethod
    def create(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def create_form(self, work_package): raise NotImplementedError

    @abstractmethod
    def create_relation(self, work_package, relation): raise NotImplementedError

    @abstractmethod
    def find_relations_by_work_package(self, work_package): raise NotImplementedError

    @abstractmethod
    def create_relation_form(self, relation): raise NotImplementedError

    @abstractmethod
    def find_watchers_by_work_package(self, work_package): raise NotImplementedError

    @abstractmethod
    def create_watcher(self, work_package, watcher): raise NotImplementedError

    @abstractmethod
    def delete_watcher(self, work_package, watcher): raise NotImplementedError

    @abstractmethod
    def find_relation_candidates_by_work_package(self, work_package, filters, query, type, pageSize): raise NotImplementedError

    @abstractmethod
    def find_available_watchers_by_work_package(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_available_projects_by_work_package(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_revisions_by_work_package(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_activities_by_work_package(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def create_activity(self, work_package, activity, notify): raise NotImplementedError