from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.delete_request import DeleteRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.attachment.attachment_command import AttachmentCommand


class Delete(AttachmentCommand):

    def __init__(self, connection, attachment):
        """Constructor for class Delete, from AttachmentCommand.

        :param connection: The connection data
        :param attachment:The attachment to delete
        """
        super().__init__(connection)
        self.attachment = attachment

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.attachment.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting attachment: {self.attachment.fileName}") from re
