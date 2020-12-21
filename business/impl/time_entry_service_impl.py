from business.impl.time_entry.delete import Delete
from business.impl.time_entry.find_between_days import FindBetweenDays
from business.impl.time_entry.find_by_context import FindByContext
from business.impl.time_entry.find_by_id import FindById
from business.time_entry_service import TimeEntryService


class TimeEntryServiceImpl(TimeEntryService):

    def find_by_context(self, context):
        find_by_context = FindByContext(context)
        return find_by_context.execute()

    def find_between_days(self, start_date, end_date):
        find_data_entries = FindBetweenDays(start_date, end_date)
        return find_data_entries.execute()

    def find_by_id(self, identifier):
        find_by_id = FindById(identifier)
        return find_by_id.execute()

    def delete(self, identifier):
        delete = Delete(identifier)
        return delete.execute()

    # TODO: Review what params we need to create a new time entry
    def new_time_entry(self): raise NotImplementedError
