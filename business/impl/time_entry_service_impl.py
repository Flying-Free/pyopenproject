from business.impl.command.time_entry.delete import Delete
from business.impl.command.time_entry.find import FindById
from business.impl.command.time_entry.find_between_days import FindBetweenDays
from business.impl.command.time_entry.find_by_context import FindByContext
from business.time_entry_service import TimeEntryService


class TimeEntryServiceImpl(TimeEntryService):

    def find_by_context(self, context):
        find_by_context = FindByContext(context)
        return find_by_context.execute()

    def find_between_days(self, start_date, end_date):
        find_data_entries = FindBetweenDays(start_date, end_date)
        return find_data_entries.execute()

    def find(self, identifier):
        find_by_id = FindById(identifier)
        return find_by_id.execute()

    def delete(self, identifier):
        delete = Delete(identifier)
        return delete.execute()

    def create(self, time_entry):
        return Create(time_entry).execute()
