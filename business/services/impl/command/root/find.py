from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.root.root_command import RootCommand
from model.root import Root


class Find(RootCommand):

    def __init__(self, root):
        self.root = root

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            return Root(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding root: {self.root}") from re
