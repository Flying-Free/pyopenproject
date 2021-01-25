from business.services.impl.command.time_entry.create import Create
from business.services.impl.command.time_entry.create_form import CreateForm
from business.services.impl.command.time_entry.delete import Delete
from business.services.impl.command.time_entry.find import Find
from business.services.impl.command.time_entry.find_all import FindAll
from business.services.impl.command.time_entry.find_between_days import FindBetweenDays
from business.services.impl.command.time_entry.find_by_context import FindByContext
from business.services.impl.command.time_entry.find_projects import FindAvailableProjects
from business.services.impl.command.time_entry.find_schema import FindSchema
from business.services.impl.command.time_entry.update_form import UpdateForm
from business.services.time_entry_service import TimeEntryService


class TimeEntryServiceImpl(TimeEntryService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_projects(self, time_entry):
        return FindAvailableProjects(self.connection).execute()

    def create_form(self, form):
        return CreateForm(self.connection, form).execute()

    def update_form(self, time_entry, form):
        return UpdateForm(self.connection, time_entry, form).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def find_between_days(self, start_date, end_date):
        return FindBetweenDays(self.connection, start_date, end_date).execute()

    def find(self, time_entry):
        return Find(self.connection, time_entry).execute()

    def delete(self, time_entry):
        return Delete(self.connection, time_entry).execute()

    def create(self, time_entry):
        return Create(self.connection, time_entry).execute()

    def find_all(self, offset, page_size, filters, sort_by):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())

    def find_schema(self):
        return FindSchema(self.connection).execute()
