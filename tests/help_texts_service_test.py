import json
import unittest

from business.services.help_texts_service import HelpTextsService


class HelpTextsServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.helpSer = HelpTextsService()
        self.help_test = json.loads('/data/help_text.json')

    def test_find(self):
        self.assertNotNull(self.helpSer.find(self.help_test))

    def test_find_all(self):
        self.assertNotNull(self.helpSer.find_all())