from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.version.version_command import VersionCommand
from model.version import Version


class FindByContext(VersionCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding version by context: {self.context}") from re
