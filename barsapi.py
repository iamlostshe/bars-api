"""Base pars module."""  # noqa: CPY001

from __future__ import annotations

import datetime as dt

import requests
from fake_useragent import UserAgent


class BarsAPI:
    """Класс для взаимодействия с API барса."""  # noqa: RUF002

    def __init__(
        self, host: str, cookie: str,
        user_agent: str | None = None,
        timeout: int | None = None,
    ) -> None:
        """Инициализация класса взаимодействия с API барса."""  # noqa: RUF002
        # Очищаем host, если необходимо
        host = host.replace("https://", "").replace("http://", "")
        if host[-1] == "/":
            host = host[:-1]

        # Генерируем ссылки
        self.get_class_year_info_url = f"https://{host}/api/SchoolService/getClassYearInfo"
        self.get_person_data_url = f"https://{host}/api/ProfileService/GetPersonData"
        self.get_school_info_url = f"https://{host}/api/SchoolService/getSchoolInfo"
        self.get_summary_marks_url = f"https://{host}/api/MarkService/GetSummaryMarks"

        # Формируем headers
        headers = {
            "user-Agent": user_agent or UserAgent().random,
            "cookie": cookie,
        }

        # Работа с timeout  # noqa: RUF003
        self.timeout = timeout or 20

        # Формируем обект сессии
        self.session = requests.Session()

        # Устанавливаем headers для сессии
        self.session.headers.update(headers)

    def get_class_year_info(self) -> dict:
        """Данные о классе ученика.

        Returns:
            Данные о классе ученика.

        """  # noqa: RUF002
        r = self.session.post(
            self.get_class_year_info_url,
            timeout=self.timeout,
        )
        return r.json()

    def get_person_data(self) -> dict:
        """Данные об ученике.

        Returns:
            Данные об ученике.

        """  # noqa: RUF002
        r = self.session.post(
            self.get_person_data_url,
            timeout=self.timeout,
        )
        return r.json()

    def get_school_info(self) -> dict:
        """Данные о школе пользователя.

        Returns:
            Данные о школе пользователя.

        """  # noqa: RUF002
        r = self.session.post(
            self.get_school_info_url,
            timeout=self.timeout,
        )
        return r.json()

    def get_summary_marks(self) -> dict:
        """Данные об оценках пользователя.

        Returns:
            Данные об оценках пользователя.

        """  # noqa: RUF002
        params = {
            "date": dt.datetime.now().strftime("%Y-%m-%d"),  # noqa: DTZ005
        }

        r = self.session.get(
            self.get_summary_marks_url,
            params=params,
            timeout=self.timeout,
        )
        return r.json()
