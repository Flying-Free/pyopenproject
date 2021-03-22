import isodate

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.time_entry.time_entry_command import TimeEntryCommand
from pyopenproject.model.form import Form


class CreateForm(TimeEntryCommand):

    def __init__(self, connection, project, work_package, activity, comment, spent_on, hours):
        super().__init__(connection)
        self.form = {
            "_links": {
                "project": {
                    "href": project.__dict__["_links"]["self"]["href"]
                },
                "activity": {
                    "href": f"/api/v3/time_entries/activities/{activity}"
                },
                "workPackage": {
                    "href": work_package.__dict__["_links"]["self"]["href"]
                }
            },
            "hours": isodate.duration_isoformat(hours),
            "comment": {
                "raw": comment
            },
            "spentOn": spent_on.strftime("%Y-%m-%d"),
        }

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/form",
                                   json=self.form).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating form: {self.form}") from re
