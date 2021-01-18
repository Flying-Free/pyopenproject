from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand
from model.attachment import Attachment


class Create(AttachmentCommand):

    def __init__(self, connection, attachment):
        super().__init__(connection)
        self.attachment = attachment

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection, context=f"{self.CONTEXT}").execute()
            return Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating attachment with id: {self.attachment.id}") from re
