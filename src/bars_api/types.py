"""Фулл типизатион."""

from dataclasses import dataclass


@dataclass
class Subperiod:
    """Четверь/полугодие/семестр."""

    code: str
    name: str


@dataclass
class SummaryMark:
    """Оценки."""

    date: str
    mark: int
    description: str


@dataclass
class TotalMark:
    """Оценка."""

    subperiod_code: str
    mark: int


class Birthday:
    """Дни рождения."""

    date: str
    short_name: str


class ClassYearInfo:
    """Информация о классе ученика."""

    @dataclass
    class Pupil:
        """Информация об ученике (класса)."""

        fullname: str
        photo: str | None
        male: bool

    class FormMaster(Pupil):
        """Информация о классном руководителе."""

    def __init__(self, json_data: dict[str, str | int | bool]) -> None:
        """Инициализация класса."""
        self.study_level: int = json_data["study_level"]
        self.letter: str = json_data["letter"]

        self.form_master = self.FormMaster(
            fullname=json_data["form_master"],
            photo=json_data["form_master_photo"],
            male=json_data["form_master_male"],
        )

        self.specialization: bool = json_data["specialization"]
        self.photo: str = json_data["photo"]
        self.pupils = [
            self.Pupil(
                fullname=p["fullname"],
                photo=p["photo"] or None,
                male=p["male"],
            )
            for p in json_data["pupils"]
        ]


class PersonData:
    """Информация о пользователе."""

    @dataclass
    class Indicator:
        """Средний балл по предмету."""

        name: str
        value: str
        css: str

    @dataclass
    class SelectedPupil:
        """Выбраный ребёнок."""

        id: int
        name: str
        ava_url: str
        school: str
        is_male: bool
        classyear: str

    @dataclass
    class User:
        """Пользователь."""

        ava_url: str
        has_ava: bool
        fullname: str
        desc: str
        is_male: bool
        phone: str
        phone_sms: str
        id: int

    def __init__(self, json_data: dict[str, str | int | bool]) -> None:
        """Инициализация сведений о пользователе."""
        self.children_persons: list = json_data["children_persons"]

        self.selected_pupil = self.SelectedPupil(
            id=json_data["selected_pupil_id"],
            name=json_data["selected_pupil_name"],
            ava_url=json_data["selected_pupil_ava_url"],
            school=json_data["selected_pupil_school"],
            is_male=json_data["selected_pupil_is_male"],
            classyear=json_data["selected_pupil_classyear"],
        )

        self.user = self.User(
            ava_url=json_data["user_ava_url"],
            has_ava=json_data["user_has_ava"],
            fullname=json_data["user_fullname"],
            desc=json_data["user_desc"],
            is_male=json_data["user_is_male"],
            phone=json_data["phone"],
            phone_sms=json_data["phone_sms"],
            id=json_data["auth_user_profile_id"],
        )

        self.indicators: list[self.Indicator] = [
            self.Indicator(
                i["name"],
                i["value"],
                i["css"],
            )
            for i in json_data["indicators"]
        ]


class SchoolInfo:
    """Информация о школе."""

    @dataclass
    class Employer:
        """Работчник школы."""

        group: str
        fullname: str
        employer_jobs: list[str]
        category: str | None
        photo: str | None
        male: bool

    def __init__(self, json_data: dict[str, str | int | bool]) -> None:
        """Инициализация школы."""
        self.name: str = json_data["name"]
        self.address: str = json_data["address"]
        self.phone: str = json_data["phone"]
        self.site_url: str = json_data["site_url"]
        self.count_employees: int = json_data["count_employees"]
        self.count_pupils: int = json_data["count_pupils"]
        self.photo: str = json_data["photo"]
        self.email: str = json_data["email"]
        self.ustav: str = json_data["ustav"]

        self.employees: list[self.Employer] = [
            self.Employer(
                group=e["group"],
                fullname=e["fullname"],
                employer_jobs=e["employer_jobs"],
                category=e["category"] or None,
                photo=e["photo"] or None,
                male=e["male"],
            )
            for e in json_data["employees"]
        ]


class SummaryMarks:
    """Краткая сводка об оценках."""

    @dataclass
    class DisciplineMarks:
        """Оценки по предмету."""

        discipline: str
        average_mark: float
        marks: list[SummaryMark]

    def __init__(self, json_data: dict[str, str | int | bool]) -> None:
        """Инициализация."""
        try:
            data = json_data["summary_marks_data"][0]

            discipline_marks = [
                self.DisciplineMarks(
                    discipline=m["discipline"],
                    average_mark=float(m["average_mark"]),
                    marks=[
                        SummaryMark(
                            date=i["date"],
                            mark=i["mark"],
                            description=i["description"],
                        )
                        for i in m["marks"]
                    ],
                )
                for m in data["discipline_marks"]
            ]
            subperiod = data["subperiod"]

            self.subperiod: Subperiod = Subperiod(
                code=subperiod["code"],
                name=subperiod["name"],
            )
            self.discipline_marks = discipline_marks
            self.dates: list[str] = data["dates"]

        except IndexError or KeyError:
            self.subperiod = None
            self.discipline_marks = []
            self.dates: list[str] = []


class TotalMarks:
    """Итоговые оценки."""

    @dataclass
    class DisciplineMark:
        """Предмет."""

        discipline: str
        period_marks: list[TotalMark]

    def __init__(self, json_data: dict[str, str | int | bool]) -> None:
        """Инициализация."""
        data = json_data["total_marks_data"][0]

        self.subperiod = [
            Subperiod(
                i["code"],
                i["name"],
            )
            for i in data["subperiods"]
        ]

        self.discipline_marks = [
            self.DisciplineMark(
                discipline=i["discipline"],
                period_marks=[
                    TotalMark(
                        m["subperiod_code"],
                        int(m["mark"]),
                    )
                    for m in i["period_marks"]
                ],
            )
            for i in data["discipline_marks"]
        ]


class Homework:
    """Домашнее задание."""

    def __init__(self) -> None:
        """Инициализация."""
        
