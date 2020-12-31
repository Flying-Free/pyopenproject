import unittest

from business.render_service import RenderService


class RenderServiceTestCase(unittest.TestCase):
    renderSer = RenderService()

    def render_request(self):
        self.assertNotNull(self.renderSer.request(1))
