from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.category.category_command import CategoryCommand
from openproject.model import category as cat


class Find(CategoryCommand):

    def __init__(self, connection, category):
        """Constructor for class Find, from CategoryCommand.

        :param connection: The connection data
        :param category: The category to find
        """
        super().__init__(connection)
        self.category = category

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.category.id}").execute()
            return cat.Category(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding category by id: {self.category.id}") from re
