import requests
from fake_useragent import UserAgent

user = UserAgent().random

login_url = "https://school.r-19.ru/auth/login"
data_url = "https://school.r-19.ru/api/ProfileService/GetPersonData"
school_url = "https://school.r-19.ru/api/SchoolService/getSchoolInfo"
class_url = "https://school.r-19.ru/api/SchoolService/getClassYearInfo"
diary_url = "https://school.r-19.ru/api/MarkService/GetSummaryMarks"

def getMarks(cookie: str):
    headers = {
        "User-Agent": user,
        "Cookie": f"sessionid={cookie}"
    }

    response = requests.post(data_url, headers=headers)
    resp = response.json()
    data = ""
    for i in resp["indicators"]:
        data += f"{i['name']} | {i['value']}\n"

    return data

def getData(cookie: str):
    headers = {
        "User-Agent": user,
        "Cookie": f"sessionid={cookie}"
    }

    response = requests.post(data_url, headers=headers)
    resp = response.json()
    data = ""
    try:
        return f"{resp['user_fullname']}\nШкола: {resp['selected_pupil_school']}"
    except Exception:
        return None
    
def getClass(cookie: str):
    headers = {
        "User-Agent": user,
        "Cookie": f"sessionid={cookie}"
    }

    response = requests.post(class_url, headers=headers)
    resp = response.json()
    data = ""
    try:
        for i in resp["pupils"]:
            data += f"{i['fullname']}\n"
        return f"Классный руководитель: {resp['form_master']}\nКласс: \n{data}"
    except Exception:
        return None    
    
def getDiary(cookie: str):
    headers = {
        "User-Agent": user,
        "Cookie": f"sessionid={cookie}"
    }

    #diary_url = f"https://school.r-19.ru/api/MarkService/GetSummaryMarks?date={str(datetime.datetime.now())}"

    '''response = requests.get(diary_url, headers=headers)
    resp = response.json()
    data = ""
    try:
        for i in resp["discipline_marks"]:
            data += f"{i['discipline']} | {i['mark']}"
        return f"{data}"
    except Exception:
        return None'''