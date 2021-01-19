import unittest

import yaml

from business.service_factory import ServiceFactory


class OpenProjectTestCase(unittest.TestCase):

    def setUp(self):
        with open("../conf/config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        url_base = cfg["api_conn"]["host"] + ":" + str(cfg["api_conn"]["port"])
        api_user = cfg["api_conn"]["user"]
        api_key = cfg["api_conn"]["password"]
        self.factory = ServiceFactory(url=url_base, user=api_user, api_key=api_key)
