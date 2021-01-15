from business.services.impl.command.help_texts.find_all import FindAll
from business.services.impl.command.help_texts.find import Find
from business.services.help_texts_service import HelpTextsServiceImpl


class HelpTextsServiceImpl(HelpTextsServiceImpl):

    def find(self, help_text):
        return Find(help_text).execute()

    def find_all(self):
        return FindAll().execute()
