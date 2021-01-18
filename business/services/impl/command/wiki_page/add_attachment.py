import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.wiki_page.wiki_command import WikiPageCommand


class AddAttachment(WikiPageCommand):

    def __init__(self, connection, work_package, attachment):
        super(connection)
        self.work_package = work_package
        self.attachment = attachment

    def execute(self):
        try:
            PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.work_package.id}/attachments",
                        json=json.dumps(self.attachment.__dict__)).execute()
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment.title}") from re
