import json

import model.relation as rel
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand


class CreateRelation(WorkPackageCommand):

    def __init__(self, connection, work_package, relation):
        super().__init__(connection)
        self.work_package = work_package
        self.relation = relation

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.work_package.id}/relations",
                                   json=json.dumps(self.relation.__dict__)).execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating relation for the work package {self.work_package.id}") from re
