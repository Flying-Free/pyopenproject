from business.services.impl.command.news.find import Find
from business.services.impl.command.news.find_all import FindAll
from business.services.news_service import NewsService


class NewsServiceImpl(NewsService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, news):
        return Find(self.connection, news).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())
