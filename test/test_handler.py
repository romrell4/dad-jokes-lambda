import unittest
from src import handler
import slack_event, alexa_event

class TestCase(unittest.TestCase):
    def test_slack(self):
        response = handler.handle(slack_event.event, None)
        self.assertEqual(200, response["statusCode"])

    def test_alexa(self):
        response = handler.handle(alexa_event.event, None)
        self.assertIsNotNone(response)
        print(response)
