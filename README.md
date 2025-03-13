# bars-api

Python библиотека для получения информации из школьного дневника bars.

## Содержание

- [Быстрый старт](#%D0%B1%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9-%D1%81%D1%82%D0%B0%D1%80%D1%82)

- [Подробно](#%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%BE)

    - [get_class_year_info](#get_class_year_info)
    - [get_person_data](#get_person_data)
    - [get_school_info](#get_school_info)
    - [get_summary_marks_url](#get_summary_marks_url)

## Быстрый старт

1. Установите [библиотеку](https://pypi.org/project/barsapi):

```bash
pip install bars-api python-dotenv
```

2. Создайте такую структуру:

```bash
your_project
├── .env
└── main.py
```

3. Скопируйте и запустите этот код:

- `.env`

```
HOST="YOUR_HOST_HERE"
COOKIE="YOUR_COOKIE_HERE"
```

- `main.py`

```python
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

        # Данные о классе пользователя  # noqa: RUF003
        c = await api.get_class_year_info()
        print(c)

        # Данные о пользователе
        p = await api.get_person_data()
        print(p)

        # Данные о школе пользователя
        s = await api.get_school_info()
        print(s)

        # Данные о оценках пользователя
        m = await api.get_summary_marks()
        print(m)


if __name__ == "__main__":
    asyncio.run(main())
```

> [!WARNING]
>
> Не забудьте заменить **YOUR_HOST_HERE** и **YOUR_COOKIE_HERE**
> на ваши данные.
>
>**YOUR_HOST_HERE** можно получить
> [тут](http://aggregator-obr.bars-open.ru/my_diary),
> а для получения **YOUR_COOKIE_HERE** воспользуйтесь
> [этим гайдом](https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25).

## Подробно

### get_class_year_info

Данные о классе ученика:

```js
{
    "study_level": 10, // Класс в котором учится пользователь
    "letter": "А", // Буква класса в котором учится пользователь
    "form_master": "Иванов Иван Иванович", // ФИО классного руководителя
    "form_master_photo": "noavatar_f_big.png", // Аватарка классного руководителя
    "form_master_male": true, // Пол классного руководителя (true - мужской, false - женский)
    "specialization": "нет", // ? Специализация
    "photo": "noavatar_big.gif", // Аватарка пользователя
    "pupils": [ // Ученики (однокласники пользователя)
        {
            "fullname": "Иванов Иван Иванович", // ФИО однокласника
            "photo": "", // Аватарка однокласника
            "male": true // Пол однокласника (true - мужской, false - женский)
        },
        ...
    ]
}
```

### get_person_data

Данные о пользователе:

```js
{
    "indicators": [ // Средний балл по предметам
        {
            "name": "Средний балл (Алгебра)", // Название предмета
            "value": "3.10", // Оценка (дробное число)
            "css": "ico orange" // Цвет, которым отображается оценка (не совсем понятно зачем, проще на фронте цвет простым "if" расчитывать)
        },
        ...
    ],


    "children_persons": [], // Дети пользователя (пустой список т. к. авторизация произведена через аккаунт ребёнка)
    "selected_pupil_id": 777777, // Внутренний id выбранного ребёнка
    "selected_pupil_name": "Иванов Иван", // ФИО выбранного ребёнка
    "selected_pupil_ava_url": "noavatar_big.png", // Аватарка выбранного ребёнка
    "selected_pupil_school": "МБОУ \"СОШ № 1\"", // Школа выбранного ребёнка
    "selected_pupil_is_male": true, // Пол выбранного ребёнка
    "selected_pupil_classyear": "10 А", // Класс выбранного ребёнка


    "user_ava_url": "noavatar_big.png", // Аватарка пользователя
    "user_has_ava": false, // Аватарка выбранного ребёнка
    "user_fullname": "Иванов Иван Иванович", // 
    "user_desc": "Ученик 10 А класса", // Описание пользователя
    "user_is_male": true, // Пол пользователя (true - мужской, false - женский)
    "phone": "", // номер телефона пользователя
    "phone_sms": "", // ? номер телефона для смс
    "auth_user_profile_id": 77777 // Внутренний id пользователя
}
```

### get_school_info

```js
{
    "name": "МБОУ СОШ № 9\" г. Город Регион", // Название школы
    "address": "ул. Пушкина, д. ...", // Адрес школы
    "phone": "+7 (777) 777-77-77", // Номер телефона школы
    "site_url": "https://github.com/iamlostshe", // Ссылка на сайт школы
    "count_employees": 91, // ??
    "count_pupils": 2067, // Общее кол-во учеников в школе
    "photo": "/jrnwfkjq.jpg", // Ссылка на фото школы
    "email": "school1@gorod.region.ru", // Электронная почта школы
    "ustav": "", // ? Устав
    "employees": [
        {
            "group": "Педагогический состав", // ? Группа (ещё есть "Обслуживающий персонал")
            "fullname": "Иванов Иван Иванович", // ФИО
            "employer_jobs": [ // Ставки
                "Классный руководитель",
                "Учитель географии"
            ],
            "category": "", // ? Категория
            "photo": "", // Ссылка на фото
            "male": true // Пол
        },
        ...
    ]
}
```

### get_summary_marks

Сводка по оценкам:

```js
{
    "subperiod": { // Текущий суб-период (зачем, непонятно...)
        "code": "Полугодие_2",
        "name": "2 Полугодие"
    },
    "discipline_marks": [
        {
            "discipline": "История", // Название предмета
            "marks": [
                {
                    "date": "2025-01-13", // Дата за которую поставлена оценка
                    "mark": "5", // Оценка (целое число)
                    "description": "Работа на уроке: нет темы" // Описание (никогда не видел другого)
                },
                ...
            ],
            "average_mark": "5.0" // Средний балл по этому предмету
        },
        ...
    ],
    "dates": [
        "2025-03-21" // ? Даты (зачем они тут, непонятно...)
        ...
    ]
}
```
