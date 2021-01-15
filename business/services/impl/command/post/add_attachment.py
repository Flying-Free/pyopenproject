import json

from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.post.post_command import PostCommand


class AddAttachment(PostCommand):

    def __init__(self, post, attachment):
        self.post = post
        self.attachment = attachment

    def execute(self):
        try:
            Connection().post(f"{self.CONTEXT}/{self.post.id}/attachments", json.dumps(self.attachment.__dict__))
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment.title}") from re
