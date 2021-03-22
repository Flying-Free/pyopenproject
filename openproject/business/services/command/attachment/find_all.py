from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.attachment.attachment_command import AttachmentCommand
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.model.attachment import Attachment


class FindAll(AttachmentCommand):

    def __init__(self, connection):
        """Constructor for class DownloadByContext, from AttachmentCommand.

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}")
            return FindListCommand(self.connection, request, class_type=Attachment).execute()
            # for attachment in json_obj["_embedded"]["elements"]:
            #     yield att.Attachment(attachment)
        except RequestError as re:
            raise BusinessError("Error finding all attachments") from re
