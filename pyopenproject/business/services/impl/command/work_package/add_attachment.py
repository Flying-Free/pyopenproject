from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand


class AddAttachment(WorkPackageCommand):

    def __init__(self, connection, work_package, attachment):
        super().__init__(connection)
        self.work_package = work_package
        self.attachment = attachment

    def execute(self):
        try:
            PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.work_package.id}/attachments",
                        json=self.attachment.__dict__).execute()
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment.title}") from re
