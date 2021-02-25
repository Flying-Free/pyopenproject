from pyopenproject import model as usr
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand


class CreateWatcher(WorkPackageCommand):

    def __init__(self, connection, work_package, user):
        super().__init__(connection)
        self.work_package = work_package
        self.watcher = {
            "user": {
                "href": f"{user.__dict__['_links']['self']['href']}"
            }
        }

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}{self.work_package.id}/watchers",
                                   json=self.watcher).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating watcher for the work package {self.work_package.id}") from re
