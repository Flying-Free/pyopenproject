from contextlib import suppress

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.patch_request import PatchRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.user.user_command import UserCommand
from pyopenproject.model import user  as usr


class Update(UserCommand):

    def __init__(self, connection, user):
        """Constructor for class Update, from UserCommand

        :param connection: The connection data
        :param user: The user to update
        """
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            user_id = self.user.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{user_id}",
                                    json=self.user.__dict__,
                                    headers={"Content-Type": "application/json"}
                                    ).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user by id: {user_id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.user.__dict__["_links"]["self"]
        with suppress(KeyError): del self.user.__dict__["_links"]["memberships"]
        with suppress(KeyError): del self.user.__dict__["id"]
        with suppress(KeyError): del self.user.__dict__["createdAt"]
        with suppress(KeyError): del self.user.__dict__["updatedAt"]
        with suppress(KeyError): del self.user.__dict__["name"]
        with suppress(KeyError): del self.user.__dict__["avatar"]
        with suppress(KeyError): del self.user.__dict__["status"]
        with suppress(KeyError): del self.user.__dict__["identityUrl"]
