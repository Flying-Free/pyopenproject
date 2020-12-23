from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.category.category_command import CategoryCommand
from model.category import Category


class FindAll(CategoryCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for work_package in json_obj._embedded.elements:
                yield Category(work_package)
        except RequestError as re:
            raise BusinessError(f"Error finding all categories") from re
