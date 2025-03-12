"""Base pars module."""  # noqa: CPY001

import datetime as dt

import requests
from fake_useragent import UserAgent

TIMEOUT = 20

USER_AGENT = UserAgent().random

HOST = "YOUR_HOST_HERE"
COOKIE = "YOUR_COOKIE_HERE"

HEADERS = {
    "user-Agent": USER_AGENT,
    "Cookie": COOKIE,
}

GET_CLASS_YEAR_INFO_URL = f"https://{HOST}/api/SchoolService/getClassYearInfo"
GET_PERSON_DATA_URL = f"https://{HOST}/api/ProfileService/GetPersonData"
GET_SCHOOL_INFO_URL = f"https://{HOST}/api/SchoolService/getSchoolInfo"
GET_SUMMARY_MARKS_URL = f"https://{HOST}/api/MarkService/GetSummaryMarks"


def get_class_year_info() -> dict:
    """Данные о классе ученика.

    Returns:
        Данные о классе ученика.

    """  # noqa: RUF002
    r = requests.post(GET_CLASS_YEAR_INFO_URL, headers=HEADERS, timeout=TIMEOUT)
    return r.json()


def get_person_data() -> dict:
    """Данные об ученике.

    Returns:
        Данные об ученике.

    """  # noqa: RUF002
    r = requests.post(GET_PERSON_DATA_URL, headers=HEADERS, timeout=TIMEOUT)
    return r.json()


def get_school_info() -> dict:
    """Данные о школе пользователя.

    Returns:
        Данные о школе пользователя.

    """  # noqa: RUF002
    r = requests.post(GET_SCHOOL_INFO_URL, headers=HEADERS, timeout=TIMEOUT)
    return r.json()


def get_summary_marks_url() -> dict:
    """Данные об оценках пользователя.

    Returns:
        Данные об оценках пользователя.

    """  # noqa: RUF002
    params = {
        "date": dt.datetime.now().strftime("%Y-%m-%d"),  # noqa: DTZ005
    }

    r = requests.get(
        url=GET_SUMMARY_MARKS_URL, headers=HEADERS,
        params=params, timeout=TIMEOUT,
    )
    return r.json()
