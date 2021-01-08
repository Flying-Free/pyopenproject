from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.attachment.attachment_command import AttachmentCommand
from model.attachment import Attachment


class Create(AttachmentCommand):

    def __init__(self, attachment):
        self.attachment = attachment

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}")
            return Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating attachment with id: {self.attachment.id}") from re
