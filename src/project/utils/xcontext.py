from typing import Dict

from django.conf import settings
from django.http import HttpRequest

from project.utils import consts
from project.utils.xdatetime import get_user_hour


def user_hour(request: HttpRequest) -> Dict[str, int]:
    hour = get_user_hour(request)
    ctx = {
        "user_hour": hour,
        "daylight_hours": consts.DAYLIGHT,
    }

    return ctx


def big_brother(_request: HttpRequest) -> Dict[str, str]:
    if settings.DEBUG:  # pragma: nocover
        return {}

    return {
        "google_analytics": consts.SCRIPT_GOOGLE_ANALYTICS,
        "google_tag_manager": consts.SCRIPT_GOOGLE_TAG_MANAGER,
        "yandex_metrika": consts.SCRIPT_YANDEX_METRIKA,
    }
