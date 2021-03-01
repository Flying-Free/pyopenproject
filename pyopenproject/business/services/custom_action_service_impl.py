from pyopenproject.business.custom_action_service import CustomActionService
from pyopenproject.business.services.command.custom_action.execute import Execute
from pyopenproject.business.services.command.custom_action.find import Find


class CustomActionServiceImpl(CustomActionService):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self, custom_action):
        return Execute(self.connection, custom_action).execute()

    def find(self, custom_action):
        return Find(self.connection, custom_action).execute()
