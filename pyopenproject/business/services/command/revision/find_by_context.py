from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.revision.revision_command import RevisionCommand
from pyopenproject.model.revision import Revision


class FindByContext(RevisionCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.context}").execute()
            return Revision(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding revision by context: {self.context}") from re
