from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.version.version_command import VersionCommand
from pyopenproject.model.form import Form


class UpdateForm(VersionCommand):

    def __init__(self, connection, form):
        """Constructor for class UpdatedForm, from VersionCommand

        :param connection: The connection data
        :param form: The form to update
        """
        super().__init__(connection)
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/form",
                                   json=self.form.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError("Error updating version form") from re
