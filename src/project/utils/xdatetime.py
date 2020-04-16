from datetime import datetime
from typing import Union

import pytz
import requests
from django.http import HttpRequest
from ipware import get_client_ip


def get_user_hour(request: HttpRequest) -> int:
    atm = datetime.now()
    hour = atm.hour

    if tz := get_user_tz(request):
        hour = pytz.utc.localize(atm).astimezone(tz).hour

    return hour


def get_user_tz(request: HttpRequest) -> Union[pytz.BaseTzInfo, None]:
    ip = get_client_ip(request)[0]
    resp = requests.get(f"http://ip-api.com/json/{ip}")
    payload = resp.json()
    tz_name = payload.get("timezone")
    if not tz_name:
        return None
    return pytz.timezone(tz_name)
