# bars-api

Python библиотека для получения информации из Школьного днвника BARS.

## Быстрый старт

```python
from barsapi import BarsAPI

# TODO: Доделать работу с HOST
HOST = "YOUR_HOST_HERE"
COOKIE = "YOUR_COOKIE_HERE"

api = BarsAPI(HOST, COOKIE)

print(api.get_class_year_info())
print(api.get_person_data())
print(api.get_school_info())
print(api.get_summary_marks_url())
```

## get_class_year_info

Данные о классе ученика:

```json
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