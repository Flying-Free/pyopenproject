import json
import unittest

from business.services.render_service import RenderService


class RenderServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.renderSer = RenderService()
        with open('./data/render.json') as f:
            self.render = Render(json.load(f))
    # TODO
    def render_request(self):
        self.assertNotNull(self.renderSer.request(1))
