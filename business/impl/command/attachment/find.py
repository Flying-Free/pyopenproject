from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.attachment.attachment_command import AttachmentCommand
from model.attachment import Attachment


class Find(AttachmentCommand):

    def __init__(self, attachment):
        self.attachment = attachment

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.attachment.id}")
            return Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding attachment by id: {self.attachment.id}") from re
