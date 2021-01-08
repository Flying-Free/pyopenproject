import unittest

from business.help_texts_service import HelpTextsService


class HelpTextsServiceTestCase(unittest.TestCase):
    helpSer = HelpTextsService()

    def test_find(self):
        self.assertNotNull(self.helpSer.find(help_test))

    def test_find_all(self):
        self.assertNotNull(self.helpSer.find_all(help_test))