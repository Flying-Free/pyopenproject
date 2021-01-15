from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.query.query_command import QueryCommand
from model.query import Query


class Find(QueryCommand):

    def __init__(self, activity,offset,pageSize,filters,columns,sortBy,groupBy,showSums,timelineVisible,timelineLabels,
                 timelineZoomLevel,highlightingMode,highlightedAttributes,showHierarchies):
        self.offset=offset
        self.pageSize=pageSize
        self.filters=filters
        self.columns=columns
        self.sortBy=sortBy
        self.groupBy=groupBy
        self.showSums=showSums
        self.timelineVisible=timelineVisible
        self.timelineLabels=timelineLabels
        self.timelineZoomLevel=timelineZoomLevel
        self.highlightingMode=highlightingMode
        self.highlightedAttributes=highlightedAttributes
        self.showHierarchies = showHierarchies
        self.activity = activity

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.activity.id}?{self.activity},{self.offset},"
                                f"{self.pageSize},{self.filters},{self.columns},{self.sortBy},{self.groupBy},"
                                f"{self.showSums},{self.timelineVisible},{self.timelineLabels},"
                                f"{self.timelineZoomLevel},{self.highlightingMode},{self.highlightedAttributes},"
                                f"{self.showHierarchies}")
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding activity by id: {self.activity.id}") from re
