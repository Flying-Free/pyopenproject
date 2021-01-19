from business.services.impl.command.news.find import Find
from business.services.impl.command.news.find_all import FindAll
from business.services.news_service import NewsService


class NewsServiceImpl(NewsService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, news):
        return Find(self.connection, news).execute()

    def find_all(self, offset, page_size, filters, sort_by):
        return FindAll(self.connection, offset, page_size, filters, sort_by).execute()
