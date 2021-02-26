from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.model import relation as rel


class CreateRelation(WorkPackageCommand):

    def __init__(self, connection, relation_type, work_package_from, work_package_to, description):
        """Constructor for class CreateRelation, from WorkPackageCommand

        :param connection: The connection data
        :param relation_type: The type of the relation
        :param work_package_from: The "from" work package in the relation
        :param work_package_to: The "to" work package in the relation
        :param description: The relation description
        """
        super().__init__(connection)
        self.work_package_from = work_package_from
        self.relation = rel.Relation(
            {
                "_type": "Relation",
                "type": f"{relation_type}",
                "from": {
                    "href": f"{work_package_from.__dict__['_links']['self']['href']}"
                },
                "to": {
                    "href": f"{work_package_to.__dict__['_links']['self']['href']}"
                },
                "description": f"{description}"
            })

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}{self.work_package_from.id}/relations",
                                   json=self.relation.__dict__).execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating relation for the work packages"
                                f" [From: {self.relation.__dict__['from']['href']}]"
                                f" [To: {self.relation.__dict__['to']['href']}]") from re
