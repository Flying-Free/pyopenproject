from abc import ABCMeta, abstractmethod


class TimeEntryService(object):
    __metaclass__ = ABCMeta

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
