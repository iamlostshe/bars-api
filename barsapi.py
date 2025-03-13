"""Base pars module."""  # noqa: CPY001

from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from aiohttp import ClientSession, ClientTimeout
from fake_useragent import UserAgent
from typing_extensions import Self

if TYPE_CHECKING:
    from types import TracebackType


class BarsAPI:
    """Класс для взаимодействия с API барса."""  # noqa: RUF002

    def __init__(
        self, host: str, cookie: str,
        user_agent: str | None = None,
        timeout: int | None = None,
    ) -> None:
        """Асинхронная инициализация класса взаимодействия с API барса."""  # noqa: RUF002
        # Очищаем host, если необходимо
        host = host.replace("https://", "").replace("http://", "")
        if host[-1] == "/":
            host = host[:-1]

        # Генерируем ссылки
        self.get_birthdays_url = f"https://{host}/api/WidgetService/getBirthdays"
        self.get_class_hours_url = f"https://{host}/api/WidgetService/getClassHours"
        self.get_class_year_info_url = f"https://{host}/api/SchoolService/getClassYearInfo"
        self.get_events_url = f"https://{host}/api/WidgetService/getEvents"
        self.get_person_data_url = f"https://{host}/api/ProfileService/GetPersonData"
        self.get_school_info_url = f"https://{host}/api/SchoolService/getSchoolInfo"
        self.get_summary_marks_url = f"https://{host}/api/MarkService/GetSummaryMarks"
        self.get_total_marks_url = f"https://{host}/api/MarkService/GetTotalMarks"

        # Формируем headers
        headers = {
            "user-Agent": user_agent or UserAgent().random,
            "cookie": cookie,
        }

        # Формируем обект сессии
        self.session = ClientSession(
            headers=headers,
            timeout=ClientTimeout(total=timeout or 20),
        )

    async def __aenter__(self) -> Self:
        """Нужен чтобы работать с with ...

        Returns:
            Self

        """  # noqa: RUF002
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        """Закрытие сессии при работе через with."""
        await self.session.close()

    async def get_birthdays(self) -> dict:
        """Данные о днёх рождения одноклассников.

        Returns:
            Данные о днёх рождения одноклассников.

        """  # noqa: RUF002
        async with self.session.post(self.get_birthdays_url) as r:
            return await r.json()

    async def get_class_hours(self) -> dict:
        """Данные о классных часах ученика/пользователя.

        Returns:
            Данные о классных часах ученика/пользователя.

        """  # noqa: RUF002
        async with self.session.post(self.get_class_hours_url) as r:
            return await r.json()

    async def get_class_year_info(self) -> dict:
        """Данные о классе ученика/пользователя.

        Returns:
            Данные о классе ученика/пользователя.

        """  # noqa: RUF002
        async with self.session.post(self.get_class_year_info_url) as r:
            return await r.json()

    async def get_events(self) -> dict:
        """Данные ивентах (предположительно о родительских собраниях или мероприятиях).

        Returns:
            Данные ивентах.

        """  # noqa: RUF002
        async with self.session.post(self.get_events_url) as r:
            return await r.json()

    async def get_person_data(self) -> dict:
        """Данные об ученике/пользователе.

        Returns:
            Данные об ученике/пользователе.

        """  # noqa: RUF002
        async with self.session.post(self.get_person_data_url) as r:
            return await r.json()

    async def get_school_info(self) -> dict:
        """Данные о школе ученика/пользователя.

        Returns:
            Данные о школе ученика/пользователя.

        """  # noqa: RUF002
        async with self.session.post(self.get_school_info_url) as r:
            return await r.json()

    async def get_summary_marks(self) -> dict:
        """Данные об оценках ученика/пользователя.

        Returns:
            Данные об оценках ученика/пользователя.

        """  # noqa: RUF002
        params = {
            "date": dt.datetime.now().strftime("%Y-%m-%d"),  # noqa: DTZ005
        }

        async with self.session.get(self.get_summary_marks_url, params=params) as r:
            return await r.json()

    async def get_total_marks(self) -> dict:
        """Данные о итоговых оценках.

        Returns:
            Данные о итоговых оценках.

        """  # noqa: RUF002
        async with self.session.post(self.get_total_marks_url) as r:
            return await r.json()
