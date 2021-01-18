from business.services.help_texts_service import HelpTextsService
from business.services.impl.command.help_texts.find import Find
from business.services.impl.command.help_texts.find_all import FindAll


class HelpTextsServiceImpl(HelpTextsService):

    def find(self, help_text):
        return Find(help_text).execute()

    def find_all(self):
        return FindAll().execute()
