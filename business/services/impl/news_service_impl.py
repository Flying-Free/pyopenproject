from business.services.news_service import NewsService
from business.services.impl.command.news.find import Find
from business.services.impl.command.news.find_all import FindAll


class NewsServiceImpl(NewsService):

    def find(self, news):
        return Find(news).execute()

    def find_all(self, offset, pageSize, filters, sortBy):
        return FindAll(offset, pageSize,filters, sortBy).execute()