from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query
from util.Filters import Filters
from util.URL import URL
from util.URLParameter import URLParameter


class Find(QueryCommand):

    def __init__(self, connection, activity, offset, pageSize, filters, columns, sortBy, groupBy, showSums,
                 timelineVisible, timelineLabels, timelineZoomLevel, highlightingMode,
                 highlightedAttributes, showHierarchies):
        super().__init__(connection)
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.columns = columns
        self.sortBy = sortBy
        self.groupBy = groupBy
        self.showSums = showSums
        self.timelineVisible = timelineVisible
        self.timelineLabels = timelineLabels
        self.timelineZoomLevel = timelineZoomLevel
        self.highlightingMode = highlightingMode
        self.highlightedAttributes = highlightedAttributes
        self.showHierarchies = showHierarchies
        self.activity = activity

    def execute(self):
        try:
            json_obj = GetRequest(self.connection,  str(URL(f"{self.CONTEXT}/{self.activity.id}",
                                          [
                                              URLParameter("offset", self.offset),
                                              URLParameter("pageSize", self.page_size),
                                              Filters("filters", self.filters),
                                              URLParameter("columns", self.columns),
                                              URLParameter("sortBy", self.sort_by),
                                              URLParameter("groupBy", self.groupBy),
                                              URLParameter("showSums", self.showSums),
                                              URLParameter("timelineVisible", self.timelineVisible),
                                              URLParameter("timelineLabels", self.timelineLabels),
                                              URLParameter("timelineZoomLevel", self.timelineZoomLevel),
                                              URLParameter("highlightingMode", self.highlightingMode),
                                              URLParameter("highlightedAttributes", self.highlightedAttributes),
                                              URLParameter("showHierarchies", self.showHierarchies)

                                          ]))).execute()

            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by id: {self.activity.id}") from re
