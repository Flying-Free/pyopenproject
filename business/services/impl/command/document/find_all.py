
from business.services.impl.command.abstract_find_all import AbstractFindAll
from model.document import Document
from util.URL import URL
from util.URLParameter import URLParameter


class FindAll(AbstractFindAll):

    def __init__(self, connection, offset, page_size, sort_by):
        """
        Constructor for class FindAll, from DocumentCommand

        :param connection: The connection data
        :param offset: The offset parameter chosen
        :param page_size: The page size parameter of the request
        :param sort_by: The sort by parameter
        """
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.sort_by = sort_by

    def cast(self, endpoint):
        return Document(endpoint)

    def request_url(self):
        return str(URL(f"{self.CONTEXT}", [
            URLParameter("offset", self.offset),
            URLParameter("pageSize", self.page_size),
            URLParameter("sortBy", self.sort_by)
        ]))
