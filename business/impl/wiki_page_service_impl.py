from business.impl.command.post.add_attachment import AddAttachment
from business.impl.command.wiki_page.find import Find
from business.impl.command.wiki_page.find_attachments import FindAttachments
from business.wiki_page_service import WikiPageService


class WikiPageServiceImpl(WikiPageService):

    def find(self, wiki_page):
        return Find(wiki_page).execute()

    def find_attachments(self, wiki):
        return FindAttachments(wiki).execute()

    def add_attachment(self, wiki, attachment):
        return AddAttachment(wiki, attachment).execute()
