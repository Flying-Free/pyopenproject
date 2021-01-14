from business.services.impl.command.priority.find import Find
from business.services.impl.command.priority.find_all import FindAll
from business.services.priority_service import PriorityService


class PriorityServiceImpl(PriorityService):

    def find(self, priority):
        return Find(priority).execute()

    def find_all(self):
        return FindAll().execute()
