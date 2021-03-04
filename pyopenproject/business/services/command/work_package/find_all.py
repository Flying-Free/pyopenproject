from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model.work_package import WorkPackage


class FindAll(WorkPackageCommand):
    def __init__(self, connection, filters, sort_by, group_by, show_sums):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by
        self.group_by = group_by
        self.show_sums = show_sums

    def execute(self):
        try:
            request = GetRequest(self.connection, str(URL(f"{self.CONTEXT}",
                                                          [
                                                              Filters(
                                                                  self.filters),
                                                              URLParameter("sortBy", self.sort_by),
                                                              URLParameter("groupBy", self.group_by),
                                                              URLParameter("showSums", self.show_sums)
                                                          ])))
            return FindListCommand(self.connection, request, WorkPackage).execute()
            # json_obj = request.execute()
            # for work_package in json_obj["_embedded"]["elements"]:
            #     yield wp.WorkPackage(work_package)
        except RequestError as re:
            raise BusinessError("Error finding all work packages") from re
