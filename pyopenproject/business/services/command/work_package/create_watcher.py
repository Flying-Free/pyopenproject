from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.model import user  as usr


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
