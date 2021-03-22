from openproject.business.news_service import NewsService
from openproject.business.services.command.news.find import Find
from openproject.business.services.command.news.find_all import FindAll


class NewsServiceImpl(NewsService):

    def __init__(self, connection):
        """Constructor for class NewsServiceImpl, from NewsService
        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self, news):
        return Find(self.connection, news).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())
