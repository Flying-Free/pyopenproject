from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.post.post_command import PostCommand
from openproject.model.attachment import Attachment


class ListAttachments(PostCommand):

    def __init__(self, connection, post):
        super().__init__(connection)
        self.post = post

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}/{self.post.id}/attachments")
            return FindListCommand(self.connection, request, Attachment).execute()
            # for attachment in json_obj["_embedded"]["elements"]:
            #     yield att.Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error getting the list of attachments of the post: {self.post.subject}") from re
