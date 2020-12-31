from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.version.version_command import VersionCommand
from model.project import Project


class Find(VersionCommand):

    def __init__(self, version):
        self.version = version

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.version.id}")
            return Project(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding version by id: {self.version.name}") from re
