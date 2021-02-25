from pyopenproject import model as att
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import AttachmentCommand


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
