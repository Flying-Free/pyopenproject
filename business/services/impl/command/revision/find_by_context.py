from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.revision.revision_command import RevisionCommand
from model.revision import Revision


class FindByContext(RevisionCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Revision(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding revision by context: {self.context}") from re
