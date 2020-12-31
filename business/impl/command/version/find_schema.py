from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.version.version_command import VersionCommand
from model.schema import Schema


class FindSchema(VersionCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/schemas")
            return Schema(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding the version schema") from re