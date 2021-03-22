from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.attachment.attachment_command import AttachmentCommand
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.model.attachment import Attachment


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
