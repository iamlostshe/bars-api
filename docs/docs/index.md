# bars-api

bars-api - это API-клиент, для взаимодействия со школьниым дневником от [`bars group`](https://bars.group), написаный на [`python`](https://python.org) и [`aiohttp`](https://github.com/aio-libs/aiohttp).

## Установка

Вы можете установить `bars-api` одним из способов ниже:

``` bash
# Используя pip
pip install git+https://github.com/imalostshe/bars-api

# Используя uv
uv pip install git+https://github.com/imalostshe/bars-api

# Используя poetry
poetry add git+https://github.com/imalostshe/bars-api
```

## Быстрый старт

0. [Устновите библиотеку](#установка).

1. Создайте такую структуру:

```bash
your_project
├── .env
└── main.py
```

2. Скопируйте и запустите этот код:

- `.env`

``` toml
HOST="YOUR_HOST_HERE"
COOKIE="YOUR_COOKIE_HERE"
```

> [!WARNING] ПРЕДУПРЕЖДЕНИЕ
>
> Не забудьте заменить `YOUR_HOST_HERE` и `YOUR_COOKIE_HERE`
> на ваши данные.
>
> `YOUR_HOST_HERE` можно получить
> [тут](https://aggregator.edu.bars.group/my_diary),
> а для получения `YOUR_COOKIE_HERE` воспользуйтесь
> [этим гайдом](https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25).

- `main.py`

```python
import asyncio
from os import getenv

from bars_api import bars_api
from dotenv import load_dotenv

# Загружаем данные из .env
load_dotenv()

# Host может быть получен здесь https://aggregator.edu.bars.group/my_diary
HOST = getenv("HOST")
COOKIE = getenv("COOKIE")


async def main() -> None:
    # Инициализируем объект API для взаимодействия
    async with bars_api(HOST, COOKIE) as api:

        print(await api.get_birthdays())
        print(await api.get_class_hours())
        print(await api.get_class_year_info())
        print(await api.get_events())
        print(await api.get_person_data())
        print(await api.get_school_info())
        print(await api.get_summary_marks())
        print(await api.get_total_marks())


if __name__ == "__main__":
    asyncio.run(main())
```
