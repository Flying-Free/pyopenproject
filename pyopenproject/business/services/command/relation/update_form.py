from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.relation.relation_command import RelationCommand
from pyopenproject.model import relation as rel


class UpdateForm(RelationCommand):

    def __init__(self, connection, relation, form):
        super().__init__(connection)
        self.relation = relation
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.relation.id}/form",
                                   json=self.form).execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form for relation {self.relation.name}") from re
