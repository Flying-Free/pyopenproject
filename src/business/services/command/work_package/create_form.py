from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.post_request import PostRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.work_package.work_package_command import WorkPackageCommand
from src.model.form import Form


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
