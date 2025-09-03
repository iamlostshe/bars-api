"""Base pars module."""

from __future__ import annotations

import datetime as dt
import json
import re
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
    SPAN_CLEANER,
    SUMMARY_MARKS_URL,
    TOTAL_MARKS_URL,
)
from .exceptions import (
    UserNotAuthenticatedError,
    ValidationError,
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
        host: str | None = None,
        cookie: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        """Асинхронная инициализация класса взаимодействия с API барса."""
        # Очищаем host, если необходимо
        if isinstance(host, str):
            host = host.replace("https://", "").rstrip("/")

        headers = {
            "user-agent": user_agent or UserAgent().random,
        }
        if cookie:
            headers["cookie"] = cookie

        # Формируем объект сессии
        self.session = ClientSession(
            base_url=f"https://{host}/api/",
            headers=headers,
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

    async def _request(self, url: str, params: dict | None = None) -> any:
        """Запрс к серверу."""
        async with self.session.post(url, params=params) as r:
            text = await r.text()

            # Проверяем ответ сервера на наличае ошибок в ответе
            if "Server.UserNotAuthenticatedError" in text or r.status == 403:
                raise UserNotAuthenticatedError

            if "Client.ValidationError" in text:
                raise ValidationError

            r.raise_for_status()

        # Преобразуем в json
        return json.loads(
            re.sub(SPAN_CLEANER, r"\1", text.replace("\u200b", "")),
        )

    async def get_regions(self) -> dict[str, str]:
        """Получаем все доступные регионы."""
        async with self.session.get(AGGREGATOR_URL) as r:
            data = await r.json()

        if data.get("success") and data.get("data"):
            return {r["name"]: r["url"].rstrip("/") for r in data["data"]}
        return None

    async def get_birthdays(self) -> list[Birthday]:
        """Данные о днёх рождения одноклассников."""
        return [
            Birthday(
                i["date"],
                i["short_name"],
            )
            for i in await self._request(BIRTHDAYS_URL)
        ]

    async def get_class_hours(self) -> dict:
        """Данные о классных часах ученика/пользователя."""
        return await self._request(CLASS_HOURS_URL)

    async def get_class_year_info(self) -> ClassYearInfo:
        """Данные о классе ученика/пользователя."""
        return ClassYearInfo(await self._request(CLASS_YEAR_INFO_URL))

    async def get_events(self) -> list:
        """Данные ивентах (родительских собраниях или мероприятиях)."""
        return await self._request(EVENTS_URL)

    async def get_person_data(self) -> PersonData:
        """Данные об ученике/пользователе."""
        return PersonData(await self._request(PERSON_DATA_URL))

    async def get_school_info(self) -> SchoolInfo:
        """Данные о школе ученика/пользователя."""
        return SchoolInfo(await self._request(SCHOOL_INFO_URL))

    async def get_summary_marks(
        self, date: dt.datetime | None = None,
    ) -> SummaryMarks:
        """Данные об оценках ученика/пользователя."""
        if not date:
            date = dt.datetime.now()

        return SummaryMarks(
            await self._request(
                SUMMARY_MARKS_URL,
                params={
                    "date": date.strftime("%Y-%m-%d"),
                },
            ),
        )

    async def get_total_marks(self) -> TotalMarks:
        """Данные о итоговых оценках."""
        return TotalMarks(await self._request(TOTAL_MARKS_URL))
