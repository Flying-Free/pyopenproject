from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.custom_object.custom_object_command import CustomObjectCommand
from model.custom_object import CustomObject


class Find(CustomObjectCommand):

    def __init__(self, custom_object):
        self.custom_object = custom_object

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.custom_object._links['self']['href']}")
            return CustomObject(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding custom_object: {self.custom_object._links['self']['href']}") from re
