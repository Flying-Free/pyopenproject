from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import TimeEntryCommand
from pyopenproject.model import Form


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
