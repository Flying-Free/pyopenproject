from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.model import work_package as wp


class FindChildren(WorkPackageCommand):
    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package
        self.obj_list=[]

    def execute(self):
        try:
            if "children" in self.work_package.__dict__["_links"]:
                for children in self.work_package.__dict__["_links"]["children"]:
                    request = GetRequest(self.connection, f'{children["href"]}')
                    self.obj_list.append(wp.WorkPackage(request.execute()))
            return self.obj_list
        except RequestError as re:
            raise BusinessError(f"Error finding children for work package {self.work_package.id}") from re
