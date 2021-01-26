import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class FindAll(ProjectCommand):
    def __init__(self, connection, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?filters={self.filters}&sortBy={self.sort_by}").execute()
            for tEntry in json_obj["_embedded"]["elements"]:
                yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all projects by context: {self.filters},{self.sort_by}") from re
