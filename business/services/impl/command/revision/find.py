from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.revision.revision_command import RevisionCommand
from model.revision import Revision


class Find(RevisionCommand):

    def __init__(self, revision):
        self.revision = revision

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.revision.id}")
            return Revision(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding revision by id: {self.revision.id}") from re
