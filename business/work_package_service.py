from abc import ABCMeta, abstractmethod


class WorkPackageService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    # TODO: Review what params we need to create a new work package
    @abstractmethod
    def new_work_package(self): raise NotImplementedError
