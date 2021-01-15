from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand


class FindWorkPackages(ProjectCommand):

    def __init__(self, project,offset,pageSize,filters,sortBy,groupBy,showSums,notify):
        self.project = project
        self.offset=offset
        self.pageSize=pageSize
        self.filters=filters
        self.sortBy=sortBy
        self.groupBy=groupBy
        self.showSums=showSums
        self.notify=notify

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.project.id}/work_packages?{self.offset},{self.pageSize},{self.filters},{self.sortBy},{self.groupBy},{self.showSums},{self.notify}")
            for budget in json_obj["_embedded"]["elements"]:
                yield WorkPackage(budget)
        except RequestError as re:
            raise BusinessError(f"Error finding workpackage by id: {self.project.name}") from re
