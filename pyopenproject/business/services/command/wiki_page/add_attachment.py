from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.wiki_page.wiki_command import WikiPageCommand


class AddAttachment(WikiPageCommand):

    def __init__(self, connection, wiki_page, attachment, file_path):
        """Constructor for class AddAttachment, from WikiPageCommand

        :param connection: The connection data
        :param wiki_page: The wiki page to add the attachment
        :param attachment: The attachment
        :param file_path: The local path to the attachment
        """
        super().__init__(connection)
        self.wiki_page = wiki_page
        self.attachment = attachment
        self.file_path = file_path

    def execute(self):
        try:
            # TODO: Add attachment file to the post
            PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.wiki_page.id}/attachments",
                        json=self.attachment.__dict__).execute()
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment.title}") from re
