from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.wiki_page.wiki_command import WikiPageCommand
from model.attachment import Attachment


class FindAttachments(WikiPageCommand):

    def __init__(self, wiki_page):
        self.wiki_page = wiki_page

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.wiki_page.id}/attachments")
            for attachment in json_obj["_embedded"]["elements"]:
                yield Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error getting the list of attachments of the wiki_page: {self.wiki_page.subject}") from re
