import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.form import Form


class UpdateForm(TimeEntryCommand):

    def __init__(self, time_entry, form):
        self.time_entry=time_entry
        self.form = form

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}/:{self.time_entry}/form", json.dumps(self.form.__dict__))
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form: {self.form.name}") from re
