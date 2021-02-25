from pyopenproject import model as cat
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import CategoryCommand


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
