import unittest

from business.help_texts_service import HelpTextsService


class HelpTextsServiceTestCase(unittest.TestCase):
    groupSer = HelpTextsService()

    def help_texts_request(self):
        self.assertNotNull(self.groupSer.request(1))
