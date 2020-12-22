from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.post.post_command import PostCommand
from model.attachment import Attachment


class ListAttachments(PostCommand):

    def __init__(self, post):
        self.post = post

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.post.id}/attachments")
            for attachment in json_obj["_embedded"]["elements"]:
                yield Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error getting the list of attachments of the post: {self.post.subject}") from re
