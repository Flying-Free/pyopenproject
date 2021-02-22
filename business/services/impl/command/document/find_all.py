from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.document.document_command import DocumentCommand
from model.document import Document
from util.URL import URL
from util.URLParameter import URLParameter


class FindAll(DocumentCommand):

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

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               URLParameter("offset", self.offset),
                                                               URLParameter("pageSize", self.page_size),
                                                               URLParameter("sortBy", self.sort_by)
                                                           ]))).execute()

            for document in json_obj["_embedded"]["elements"]:
                yield Document(document)
        except RequestError as re:
            raise BusinessError(f"Error finding all documents") from re
