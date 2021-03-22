from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.attachment.attachment_command import AttachmentCommand
from openproject.model import attachment as att


class Find(AttachmentCommand):

    def __init__(self, connection, attachment):
        """Constructor for class Find, from AttachmentCommand.

        :param connection: The connection data
        :param attachment: The attachment to find
        """
        super().__init__(connection)
        self.attachment = attachment

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.attachment.id}").execute()
            return att.Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding attachment by id: {self.attachment.id}") from re
