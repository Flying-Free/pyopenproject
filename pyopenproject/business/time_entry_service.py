from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class TimeEntryService(AbstractService):
    """
    Class TimeEntryService,
    service for time entry endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find_by_context(self, context): raise NotImplementedError

    @abstractmethod
    def find_between_days(self, start_date, end_date): raise NotImplementedError

    @abstractmethod
    def find(self, time_entry): raise NotImplementedError

    @abstractmethod
    def delete(self, time_entry): raise NotImplementedError

    @abstractmethod
    def create(self, time_entry): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset, page_size, filters, sort_by): raise NotImplementedError

    @abstractmethod
    def find_schema(self): raise NotImplementedError

    @abstractmethod
    def create_form(self, project, work_package, activity, comment, spent_on, hours): raise NotImplementedError

    @abstractmethod
    def update_form(self, form): raise NotImplementedError

    @abstractmethod
    def find_projects(self, time_entry): raise NotImplementedError
