from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand
from pyopenproject.model import Form


class CreateForm(WorkPackageCommand):

    def __init__(self, connection):
        """Constructor for class CreateForm, from WorkPackageCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/hal+json"},
                                   context=f"{self.CONTEXT}form").execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating work package form") from re
