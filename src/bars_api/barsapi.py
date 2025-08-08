"""Base pars module."""

from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, Self

from aiohttp import ClientSession, ClientTimeout
from fake_useragent import UserAgent

from .consts import (
    BIRTHDAYS_URL,
    CLASS_HOURS_URL,
    CLASS_YEAR_INFO_URL,
    EVENTS_URL,
    PERSON_DATA_URL,
    SCHOOL_INFO_URL,
    SUMMARY_MARKS_URL,
    TOTAL_MARKS_URL,
)

if TYPE_CHECKING:
    from types import TracebackType


class BarsAPI:
    """Класс для взаимодействия с API барса."""

    def __init__(
        self,
        host: str,
        cookie: str,
        user_agent: str | None = None,
        timeout: int | None = None,
    ) -> None:
        """Асинхронная инициализация класса взаимодействия с API барса."""
        # Формируем headers
        headers = {
            "user-Agent": user_agent or UserAgent().random,
            "cookie": cookie,
        }

        # Очищаем host, если необходимо
        host = host.replace("https://", "").replace("http://", "")
        if host[-1] == "/":
            host = host[:-1]

        # Получаем base_url
        base_url = "https://{host}/api/"

        # Формируем обект сессии
        self.session = ClientSession(
            base_url=base_url,
            headers=headers,
            timeout=ClientTimeout(total=timeout or 20),
        )

    async def __aenter__(self) -> Self:
        """Нужен чтобы работать с with ...

        Returns:
            Self

        """
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
        """Данные о днёх рождения одноклассников."""
        async with self.session.post(BIRTHDAYS_URL) as r:
            return await r.json()

    async def get_class_hours(self) -> dict:
        """Данные о классных часах ученика/пользователя."""
        async with self.session.post(CLASS_HOURS_URL) as r:
            return await r.json()

    async def get_class_year_info(self) -> dict:
        """Данные о классе ученика/пользователя."""
        async with self.session.post(CLASS_YEAR_INFO_URL) as r:
            return await r.json()

    async def get_events(self) -> dict:
        """Данные ивентах (родительских собраниях или мероприятиях)."""
        async with self.session.post(EVENTS_URL) as r:
            return await r.json()

    async def get_person_data(self) -> dict:
        """Данные об ученике/пользователе."""
        async with self.session.post(PERSON_DATA_URL) as r:
            return await r.json()

    async def get_school_info(self) -> dict:
        """Данные о школе ученика/пользователя."""
        async with self.session.post(SCHOOL_INFO_URL) as r:
            return await r.json()

    async def get_summary_marks(self) -> dict:
        """Данные об оценках ученика/пользователя."""
        async with self.session.get(
            SUMMARY_MARKS_URL,
            params={
                "date": dt.datetime.now().strftime("%Y-%m-%d"),
            },
        ) as r:
            return await r.json()

    async def get_total_marks(self) -> dict:
        """Данные о итоговых оценках."""
        async with self.session.post(TOTAL_MARKS_URL) as r:
            return await r.json()
