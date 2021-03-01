from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model import relation as rel


class FindRelationCandidates(WorkPackageCommand):
    def __init__(self, connection, work_package, filters, query, work_package_type, page_size):
        """Constructor for class FindRelationCandidates, from WorkPackageCommand
        :param connection: The connection data
        :param work_package: The work package
        :param filters: The filters parameter
        :param query: The query parameter
        :param work_package_type: The work_package type as parameter
        :param page_size: The page size parameter
        """
        super().__init__(connection)
        self.work_package = work_package
        self.filters = filters
        self.query = query
        self.type = work_package_type
        self.pageSize = page_size

    def execute(self):
        try:
            json_obj = GetRequest(connection=self.connection,
                                  context=str(URL(f"{self.CONTEXT}"
                                                  f"{self.work_package.id}/available_relation_candidates",
                                                  [
                                                      Filters(
                                                          self.filters),
                                                      URLParameter
                                                      ("query", self.query),
                                                      URLParameter
                                                      ("type", self.type),
                                                      URLParameter
                                                      ("pageSize", self.pageSize)
                                                  ]))).execute()

            for relation in json_obj["_embedded"]["elements"]:
                yield rel.Relation(relation)
        except RequestError as re:
            raise BusinessError(f"Error finding relation candidates for work package {self.work_package.id}") from re
