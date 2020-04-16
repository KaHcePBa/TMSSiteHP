from unittest import TestCase
from unittest.mock import patch

from django.http import HttpRequest

from project.utils.xcontext import user_hour


class Test(TestCase):
    @patch("project.utils.xcontext.get_user_hour")
    def test_user_hour(self, mock_get_user_hour):
        mock_get_user_hour.return_value = 12
        ret = user_hour(HttpRequest())
        self.assertDictEqual(ret, {"user_hour": 12, "daylight_hours": range(9, 21)})
