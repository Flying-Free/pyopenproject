import json
import unittest

from business.services.render_service import RenderService


class RenderServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.renderSer = RenderService()
        self.render = json.loads('/data/render.json')

    def render_request(self):
        self.assertNotNull(self.renderSer.request(1))
