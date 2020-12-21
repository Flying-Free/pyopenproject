from src.extract.business.service_factory import ServiceFactory


class Documents:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_attachments(self):
        if self._links.attachments.href is not None:
            return ServiceFactory.get_attachment_service().find_by_context(self._links.attachments.href)
        return None

    def get_project(self):
        if self._links.project.href is not None:
            return ServiceFactory.get_project_service().find_by_context(self._links.project.href)
        return None

    # TODO
    #         "addAttachment": {
    #             "href": "/api/v3/documents/1/attachments",
    #             "method": "post"
    #         }
