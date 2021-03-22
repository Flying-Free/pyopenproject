from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.document.document_command import DocumentCommand
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model.document import Document


class FindAll(DocumentCommand):

    def __init__(self, connection, sort_by):
        """Constructor for class FindAll, from DocumentCommand.

        :param connection: The connection data
        :param offset: The offset parameter chosen
        :param page_size: The page size parameter of the request
        :param sort_by: The sort by parameter
        """
        super().__init__(connection)
        self.sort_by = sort_by

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                           [
                                                               URLParameter
                                                               ("sortBy", self.sort_by)
                                                           ])))
            return FindListCommand(self.connection, request, Document).execute()
            # for document in json_obj["_embedded"]["elements"]:
            #     yield Document(document)
        except RequestError as re:
            raise BusinessError("Error finding all documents") from re
