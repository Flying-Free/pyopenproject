from abc import ABCMeta, abstractmethod


class TimeEntryService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_context(self): raise NotImplementedError

    @abstractmethod
    def find_between_days(self, start_date, end_date): raise NotImplementedError

    @abstractmethod
    def find_by_id(self, identifier): raise NotImplementedError

    @abstractmethod
    def delete(self, identifier): raise NotImplementedError

    # TODO: Review what params we need to create a new time entry
    @abstractmethod
    def new_time_entry(self): raise NotImplementedError
