import json

from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import WorkPackageCommand
from pyopenproject.model import Form


class CreateRelationForm(WorkPackageCommand):

    def __init__(self, connection, work_package, relation):
        super().__init__(connection)
        self.work_package = work_package
        self.relation = relation

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.work_package.id}/form",
                                   json=json.dumps(self.relation.__dict__)).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating relation for work package {self.work_package.id}") from re
