import json

import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class FindParents(ProjectCommand):

    def __init__(self, connection, filters, of, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.of = of
        self.sortBy = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,
                                  f"{self.CONTEXT}/available_parent_projects?{self.filters},{self.of},{self.sortBy}")\
                .execute()
            for tEntry in json.loads(json_obj):
                yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding parents of project: {self.project.name}") from re
