from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand
from model.attachment import Attachment


class FindAll(AttachmentCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for attachment in json_obj._embedded.elements:
                yield Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error finding all attachments") from re
