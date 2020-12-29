from business.impl.command.root.find import Find
from business.root_service import RootService


class RootServiceImpl(RootService):

    def find(self):
        return Find().execute()

