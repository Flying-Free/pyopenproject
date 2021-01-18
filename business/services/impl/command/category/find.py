from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.category.category_command import CategoryCommand
from model.category import Category


class Find(CategoryCommand):

    def __init__(self, connection, category):
        super(connection)
        self.category = category

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.category.id}").execute()
            return Category(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding category by id: {self.category.id}") from re
