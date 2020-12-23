from business.impl.command.post.add_attachment import AddAttachment
from business.impl.command.post.list_attachments import ListAttachments
from business.wiki_page_service import WikiPageService


class WikiPageServiceImpl(WikiPageService):

    def list_attachments(self, wiki):
        return ListAttachments(wiki).execute()

    def add_attachment(self, wiki, attachment):
        return AddAttachment(wiki, attachment).execute()
