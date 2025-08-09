## 1. Initial commit | Коммит инициализации

- Создан `README.md`.

## 2. Update README.md | Обновление README.md

- В `README.md` обавлен пример использования:

```py
import barsapi

getMarks(cookie)
getData(cookie)
getClass(cookie)
```

## 3. project | add code from pypi | Добавлен код с PyPI

- Добавлен код с [`PyPI`](https://pypi.org/project/barsapi/).

## 4. project | add ruff code linter | Добавлен ruff линтер

- Добавлен ruff линтер (его конфиг).

## 5. code | standartizate to pep-8 | Код стандартизирован

- Код приведён к более чистому стилю.
- Создан `.gitignore`.
- Создан `requirements.txt`.

## 6. readme | writed docs | Написана документация

- Написана мини-документация в `README.md`/

## 7. project | add todo | Добавлены планы

- Создан файл `TODO.md`.
- Записаны основные задачи.

## 8. code | rewrite to one class structure | Переписан по структру одного класса

- Пакет теперь может так:

```py
from barsapi import BarsAPI

HOST = "YOUR_HOST_HERE"
COOKIE = "YOUR_COOKIE_HERE"

api = BarsAPI(HOST, COOKIE)

print(api.get_class_year_info())
print(api.get_person_data())
print(api.get_school_info())
print(api.get_summary_marks())
```

## 9. code | rewrited to aiohttp | Переписан на aiohttp

- Код переписан под парсинг через `aiohttp`.
- Код теперь полностью асинхронный.
- Реализована возможность работы черех `with`:

```py
import asyncio
from os import getenv

from barsapi import BarsAPI
from dotenv import load_dotenv

# Загружаем данные из .env
load_dotenv()

# Host может быть получен здесь http://aggregator-obr.bars-open.ru/my_diary
HOST = getenv("HOST")
COOKIE = getenv("COOKIE")


async def main() -> None:
    # Инициализируем объект API для взаимодействия
    async with BarsAPI(HOST, COOKIE) as api:
        print(await api.get_total_marks())


if __name__ == "__main__":
    asyncio.run(main())
```

## 10. project | add license | Добавлена лицензия

- Добавлена MIT лицензия.

## 11. code | add new functions | Добавлены новые функции

- Добавлены 4 новые функции:
    - get_birthdays()
    - get_class_hours()
    - get_events_url()
    - get_total_marks_url()

## 12. project | update pyproject.toml | Обновлён pyproject.toml

- Указанна обновлённая версия.
- Указаны авторы в новом формате.
- Указаны правильные зависимости (ранее пакет был переписан под `aiohttp`, а также добавлен `typing_extensions`).
- Версия `python` указана в правильном формате (`requires-python = ">=3.11"`).
- Укащана лицензия (`license = "MIT"`).
- Указаны ссылки на проект:

```toml
[project.urls]
Homepage = "https://github.com/iamlostshe/bars-api"
# Documentation = "https://readthedocs.org"
Repository = "https://github.com/iamlostshe/bars-api.git"
"Bug Tracker" = "https://github.com/iamlostshe/bars-api/issues"
Changelog = "https://github.com/iamlostshe/bars-api/CHANGELOG.md"
```

## 13. project | add CHANGELOG.md | Создан CHANGELOG.md

- Создан CHANGELOG.md.
- В нём указана все изменения в проекте за всё время.

## 14. project | fix structure | Исправлена структура

- Проект приведён к стандартной структуре PyPI репозитрия:

```bash
.
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
├── README.md
├── src
│   └── bars_api
│       ├── barsapi.py
│       └── __init__.py
├── tests
└── TODO.md
```

## 15. Проект оптимизирован

- Обновлён конфиг ruff-а.
- Обновлён .gitignore.
- Добавлены настройки vs code.

- Оптимизирован парсер.
