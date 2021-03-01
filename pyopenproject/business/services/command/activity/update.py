from contextlib import suppress

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.patch_request import PatchRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.activity.activity_command import ActivityCommand
from pyopenproject.model import activity as act


class Update(ActivityCommand):

    def __init__(self, connection, activity):
        """Constructor for class Update, from ActivityCommand

        :param connection: The connection data
        :param activity: The activity we want to update
        """
        super().__init__(connection)
        self.activity = activity

    def execute(self):
        try:
            activity_id = self.activity.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{activity_id}",
                                    json=self.activity.__dict__).execute()

            return act.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating activity: {activity_id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.activity.__dict__["_type"]
        with suppress(KeyError): del self.activity.__dict__["_links"]
        with suppress(KeyError): del self.activity.__dict__["id"]
        with suppress(KeyError): del self.activity.__dict__["details"]
        with suppress(KeyError): del self.activity.__dict__["comment"]["format"]
        with suppress(KeyError): del self.activity.__dict__["comment"]["html"]
        with suppress(KeyError): del self.activity.__dict__["createdAt"]
        with suppress(KeyError): del self.activity.__dict__["version"]
