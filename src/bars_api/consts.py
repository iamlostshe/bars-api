"""Некоторые постоянные значения."""

# Ссылки на различнве разделы
BIRTHDAYS_URL = "WidgetService/getBirthdays"
CLASS_HOURS_URL = "WidgetService/getClassHours"
CLASS_YEAR_INFO_URL = "SchoolService/getClassYearInfo"
EVENTS_URL = "WidgetService/getEvents"
PERSON_DATA_URL = "ProfileService/GetPersonData"
SCHOOL_INFO_URL = "SchoolService/getSchoolInfo"
SUMMARY_MARKS_URL = "MarkService/GetSummaryMarks"
TOTAL_MARKS_URL = "MarkService/GetTotalMarks"
HOMEWORK_URL = "HomeworkService/GetHomeworkFromRange"

# Ссылка на страницу со ссылками на все сервера дневников в разных регионах
# old_url: http://aggregator-obr.bars-open.ru/my_diary
AGGREGATOR_URL = "https://aggregator.edu.bars.group/my_diary"

# Регулярное выражение для удаления (экранирования) тегов <span>
SPAN_CLEANER = r"<span[^>]*>(.*?)</span>"
