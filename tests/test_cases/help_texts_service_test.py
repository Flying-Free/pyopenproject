import json
import os

from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.model.help_text import HelpText
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class HelpTextsServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        DATA = os.path.join(self.TEST_CASES, '../data/help_text.json')
        self.helpSer = self.op.get_help_texts_service()
        with open(DATA) as f:
            self.help_text = HelpText(json.load(f))

    def test_not_found(self):
        # There's no help text --> Exception
        with self.assertRaises(BusinessError):
            self.helpSer.find(self.help_text)

    def test_find(self):
        # TODO: We need to create Help Texts using the API
        pass

    def test_find_all(self):
        help_texts = self.helpSer.find_all()
        # There's not any help text in the basic installation
        self.assertEqual(0, len(help_texts))
