import os
import unittest

import yaml

from pyopenproject.openproject import OpenProject


class OpenProjectTestCase(unittest.TestCase):
    TEST_CASES = os.path.dirname(os.path.abspath(__file__))
    CONFIG = os.path.join(TEST_CASES, '../conf/config.yml')

    def setUp(self):
        with open(self.CONFIG, "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        url_base = cfg["api_conn"]["host"] + ":" + str(cfg["api_conn"]["port"])
        api_user = cfg["api_conn"]["user"]
        api_key = cfg["api_conn"]["password"]
        self.op = OpenProject(url=url_base, user=api_user, api_key=api_key)
