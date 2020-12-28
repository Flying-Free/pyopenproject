from business.news_service import NewsService
from business.impl.command.news.find import Find
from business.impl.command.news.find_all import FindAll


class DocumentServiceImpl(NewsService):

    def find(self, news):
        return Find(news).execute()

    def find_all(self, offset, pageSize,filters, sortBy):
        return FindAll(offset, pageSize,filters, sortBy).execute()