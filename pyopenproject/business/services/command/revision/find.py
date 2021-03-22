from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.revision.revision_command import RevisionCommand
from pyopenproject.model import revision as r


class Find(RevisionCommand):

    def __init__(self, connection, revision):
        super().__init__(connection)
        self.revision = revision

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.revision.id}").execute()
            return r.Revision(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding revision by id: {self.revision.id}") from re
