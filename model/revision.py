import business.service_factory as service_factory


class Revision:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def get_project(self):
        if self._links.project.href is not None:
            return service_factory.ServiceFactory.get_project_service()\
                .find_by_context(self._links.project.href)
        return None

    def get_author(self):
        if self._links.author.href is not None:
            return service_factory.ServiceFactory.get_user_service()\
                .find_by_context(self._links.author.href)
        return None

    def show_revision(self):
        if self._links.showRevision.href is not None:
            return service_factory.ServiceFactory.get_project_service()\
                .find_by_context(self._links.showRevision.href)
        return None

    def __str__(self):
        return self.__dict__
