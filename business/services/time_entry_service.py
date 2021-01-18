from abc import ABCMeta, abstractmethod


class TimeEntryService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super

    @abstractmethod
    def find_by_context(self): raise NotImplementedError

    @abstractmethod
    def find_between_days(self, start_date, end_date): raise NotImplementedError

    @abstractmethod
    def find(self, time_entry): raise NotImplementedError

    @abstractmethod
    def delete(self, identifier): raise NotImplementedError

    @abstractmethod
    def create(self): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset,pageSize,filters,sortBy): raise NotImplementedError

    @abstractmethod
    def find_schema(self, time_entry): raise NotImplementedError

    @abstractmethod
    def create_form(self, form): raise NotImplementedError

    @abstractmethod
    def update_form(self, time_entry, form): raise NotImplementedError

    @abstractmethod
    def find_projects(self, time_entry): raise NotImplementedError