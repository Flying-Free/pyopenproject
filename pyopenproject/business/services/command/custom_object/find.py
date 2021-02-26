from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.custom_object.custom_object_command import CustomObjectCommand
from pyopenproject.model.custom_object import CustomObject


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
