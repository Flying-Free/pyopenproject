import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
from model.form import Form


class CreateForm(TimeEntryCommand):

    def __init__(self, connection, form):
        super(connection)
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/form",
                                   json=json.dumps(self.form.__dict__)).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating form: {self.form.name}") from re
