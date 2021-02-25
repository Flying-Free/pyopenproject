from pyopenproject import model as r
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand


class FindRevisions(WorkPackageCommand):
    def __init__(self, connection, work_package):
        super().__init__(connection)
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.work_package.id}/revisions").execute()
            for revision in json_obj["_embedded"]["elements"]:
                yield r.Revision(revision)
        except RequestError as re:
            raise BusinessError(f"Error finding revisions for work package {self.work_package.id}") from re