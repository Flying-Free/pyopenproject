from pyopenproject import model as r
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import RevisionCommand


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
