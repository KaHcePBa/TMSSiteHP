from unittest import TestCase
from unittest.mock import patch

import pytz
import requests
from django.http import HttpRequest
from freezegun import freeze_time

from project.utils.xdatetime import get_user_hour
from project.utils.xdatetime import get_user_tz


class MockRequestsResponse:
    def __init__(self, json):
        self.__json = json

    def json(self):
        return self.__json


class Test(TestCase):
    @freeze_time("2020-01-01 12:00:00")
    @patch("project.utils.xdatetime.get_user_tz")
    def test_get_user_hour(self, mock_get_user_tz):
        mock_get_user_tz.return_value = None
        ret = get_user_hour(HttpRequest())
        self.assertEqual(ret, 12)

        mock_get_user_tz.return_value = pytz.timezone("Europe/Minsk")
        ret = get_user_hour(HttpRequest())
        self.assertEqual(ret, 15)

    @freeze_time("2020-01-01 12:00:00")
    @patch("project.utils.xdatetime.get_client_ip")
    @patch.object(requests, requests.get.__name__)
    def test_get_user_tz(self, mock_requests_get, mock_get_client_ip):
        mock_get_client_ip.return_value = [None]

        mock_requests_get.return_value = MockRequestsResponse({"timezone": "UTC"})
        ret = get_user_tz(HttpRequest())
        self.assertEqual(ret, pytz.timezone("UTC"))

        mock_requests_get.return_value = MockRequestsResponse({})
        ret = get_user_tz(HttpRequest())
        self.assertIsNone(ret)
