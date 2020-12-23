from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.work_package.work_package_command import WorkPackageCommand
from model.attachment import Attachment


class ListAttachments(WorkPackageCommand):

    def __init__(self, work_package):
        self.work_package = work_package

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.work_package.id}/attachments")
            for attachment in json_obj["_embedded"]["elements"]:
                yield Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error getting the list of attachments of the work_package: {self.work_package.subject}") from re
