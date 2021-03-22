from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.query.query_command import QueryCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model.query import Query


class Find(QueryCommand):

    def __init__(self, connection, activity, offset, page_size, filters, columns, sort_by, group_by, show_sums,
                 timeline_visible, timeline_labels, timeline_zoom_level, highlighting_mode,
                 highlighted_attributes, show_hierarchies):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.columns = columns
        self.sort_by = sort_by
        self.group_by = group_by
        self.show_sums = show_sums
        self.timeline_visible = timeline_visible
        self.timeline_labels = timeline_labels
        self.timeline_zoom_level = timeline_zoom_level
        self.highlighting_mode = highlighting_mode
        self.highlighted_attributes = highlighted_attributes
        self.show_hierarchies = show_hierarchies
        self.activity = activity

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, str(URL(f"{self.CONTEXT}/{self.activity.id}",
                                                           [
                                                               URLParameter
                                                               ("offset", self.offset),
                                                               URLParameter
                                                               ("pageSize", self.page_size),
                                                               Filters(
                                                                   self.filters),
                                                               URLParameter
                                                               ("columns", self.columns),
                                                               URLParameter
                                                               ("sortBy", self.sort_by),
                                                               URLParameter
                                                               ("groupBy", self.group_by),
                                                               URLParameter
                                                               ("showSums", self.show_sums),
                                                               URLParameter
                                                               ("timelineVisible", self.timeline_visible),
                                                               URLParameter
                                                               ("timelineLabels", self.timeline_labels),
                                                               URLParameter
                                                               ("timelineZoomLevel",
                                                                self.timeline_zoom_level),
                                                               URLParameter
                                                               ("highlightingMode", self.highlighting_mode),
                                                               URLParameter
                                                               ("highlightedAttributes",
                                                                self.highlighted_attributes),
                                                               URLParameter
                                                               ("showHierarchies", self.show_hierarchies)

                                                           ]))).execute()

            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by id: {self.activity.id}") from re
