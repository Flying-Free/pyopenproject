from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from pyopenproject.model.form import Form


class UpdateForm(TimeEntryCommand):

    def __init__(self, connection, form):
        super().__init__(connection)
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   # context=f"{self.CONTEXT}/:{self.time_entry}/form",
                                   context=f"{self.CONTEXT}/form",
                                   json=self.form.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form: {self.form.name}") from re
