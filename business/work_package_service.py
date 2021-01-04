from abc import ABCMeta, abstractmethod


class WorkPackageService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def method(self): raise NotImplementedError

    @abstractmethod
    def find(self, notify): raise NotImplementedError

    @abstractmethod
    def update_work_package(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def delete_work_package(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def find_schema(self, identifier): raise NotImplementedError

    @abstractmethod
    def find_all_schemas(self, filters): raise NotImplementedError

    @abstractmethod
    def update_work_package_form(self, work_package): raise NotImplementedError

    @abstractmethod
    def find_all(self, notify, offset, pageSize,filters, sortBy, groupBy, showSums): raise NotImplementedError

    @abstractmethod
    def new_work_package(self, work_package, notify): raise NotImplementedError

    @abstractmethod
    def new_work_package_form(self): raise NotImplementedError

    #belongs to /project context
    #@abstractmethod
    #def find_by_project(self, project, offset, pageSize, filters, sortBy, groupBy, showSums, notify): raise NotImplementedError

    @abstractmethod
    def new_relation(self, work_package, relation): raise NotImplementedError

    @abstractmethod
    def find_relations_by_work_package(self, work_package): raise NotImplementedError

    @abstractmethod
    def new_relation_form(self, relation): raise NotImplementedError

    @abstractmethod
    def find_watchers_by_work_package(self): raise NotImplementedError

    @abstractmethod
    def new_watcher(self, work_package, watcher): raise NotImplementedError

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
    def new_activity(self, work_package, activity, notify): raise NotImplementedError

    # belongs to /project context
    #@abstractmethod
    #def find_available_assignees_by_work_package(self, project, work_package): raise NotImplementedError

    # belongs to /project context
    #@abstractmethod
    #def find_available_responsibles_by_work_package(self, project, work_package): raise NotImplementedError
