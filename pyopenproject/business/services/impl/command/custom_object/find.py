from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import CustomObjectCommand
from pyopenproject.model import CustomObject


class Find(CustomObjectCommand):

    def __init__(self, connection, custom_object):
        """Constructor for class Find, from CustomObjectCommand.

        :param connection: The connection data
        :param custom_object: The custom object to find
        """
        super().__init__(connection)
        self.custom_object = custom_object

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.custom_object.__dict__['_links']['self']['href']}").execute()
            return CustomObject(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding custom_object:"
                                f" {self.custom_object.__dict__['_links']['self']['href']}") from re
