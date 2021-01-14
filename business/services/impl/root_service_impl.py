from business.services.impl.command.root.find import Find
from business.services.root_service import RootService


class RootServiceImpl(RootService):

    def find(self):
        return Find().execute()

