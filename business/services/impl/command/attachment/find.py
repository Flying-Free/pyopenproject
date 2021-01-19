import model.attachment as att
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand


class Find(AttachmentCommand):

    def __init__(self, connection, attachment):
        super().__init__(connection)
        self.attachment = attachment

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.attachment.id}").execute()
            return att.Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding attachment by id: {self.attachment.id}") from re
