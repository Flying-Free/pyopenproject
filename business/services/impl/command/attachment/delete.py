from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand


class Delete(AttachmentCommand):

    def __init__(self, attachment):
        self.attachment = attachment

    def execute(self):
        try:
            Connection().delete(f"{self.CONTEXT}/{self.attachment.id}")
        except RequestError as re:
            raise BusinessError(f"Error deleting attachment: {self.attachment.title}") from re
