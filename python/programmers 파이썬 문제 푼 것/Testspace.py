from datetime import datetime

def solution(a, b):
    date_string = "2016{}{}".format(a, b)
    date_format = "%Y%m%d"
    date_time = datetime.strptime(date_string, date_format)
    result = date_time.weekday()
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return day[result].upper()