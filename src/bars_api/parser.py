"""Base pars module."""

from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, Self

from aiohttp import ClientSession
from fake_useragent import UserAgent

from .consts import (
    AGGREGATOR_URL,
    BIRTHDAYS_URL,
    CLASS_HOURS_URL,
    CLASS_YEAR_INFO_URL,
    EVENTS_URL,
    PERSON_DATA_URL,
    SCHOOL_INFO_URL,
    SUMMARY_MARKS_URL,
    TOTAL_MARKS_URL,
)
from .types import (
    Birthday,
    ClassYearInfo,
    PersonData,
    SchoolInfo,
    SummaryMarks,
    TotalMarks,
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
    ) -> None:
        """Асинхронная инициализация класса взаимодействия с API барса."""
        # Очищаем host, если необходимо
        host = host.replace("https://", "")
        if host[-1] == "/":
            host = host[:-1]

        # Формируем объект сессии
        self.session = ClientSession(
            base_url=f"https://{host}/api/",
            headers={
                "user-Agent": user_agent or UserAgent().random,
                "cookie": cookie,
            },
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
    ) -> None:
        """Закрытие сессии при работе через with."""
        await self.session.close()

    async def get_regions(self) -> dict[str, str]:
        """Получаем все доступные регионы."""
        async with self.session.get(AGGREGATOR_URL) as r:
            data = await r.json()

        if data.get("success") and data.get("data"):
            return {r["name"]: r["url"].rstrip("/") for r in data["data"]}
        return None

    async def get_birthdays(self) -> list[Birthday]:
        """Данные о днёх рождения одноклассников."""
        async with self.session.post(BIRTHDAYS_URL) as r:
            return [
                Birthday(
                    i["date"],
                    i["short_name"],
                ) for i in await r.json()
            ]

    async def get_class_hours(self) -> dict:
        """Данные о классных часах ученика/пользователя."""
        async with self.session.post(CLASS_HOURS_URL) as r:
            return await r.json()

    async def get_class_year_info(self) -> ClassYearInfo:
        """Данные о классе ученика/пользователя."""
        async with self.session.post(CLASS_YEAR_INFO_URL) as r:
            return ClassYearInfo(await r.json())

    async def get_events(self) -> list:
        """Данные ивентах (родительских собраниях или мероприятиях)."""
        async with self.session.post(EVENTS_URL) as r:
            return await r.json()

    async def get_person_data(self) -> PersonData:
        """Данные об ученике/пользователе."""
        async with self.session.post(PERSON_DATA_URL) as r:
            return PersonData(await r.json())

    async def get_school_info(self) -> SchoolInfo:
        """Данные о школе ученика/пользователя."""
        async with self.session.post(SCHOOL_INFO_URL) as r:
            return SchoolInfo(await r.json())

    async def get_summary_marks(self) -> SummaryMarks:
        """Данные об оценках ученика/пользователя."""
        async with self.session.get(
            SUMMARY_MARKS_URL,
            params={
                "date": dt.datetime.now().strftime("%Y-%m-%d"),
            },
        ) as r:
            return SummaryMarks(await r.json())

    async def get_total_marks(self) -> TotalMarks:
        """Данные о итоговых оценках."""
        async with self.session.post(TOTAL_MARKS_URL) as r:
            return TotalMarks(await r.json())
