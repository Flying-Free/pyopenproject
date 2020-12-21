import json

from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.project.project_command import ProjectCommand
from src.extract.model.project import Project


class FindAll(ProjectCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for tEntry in json.loads(json_obj):
                yield Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.context}") from re
