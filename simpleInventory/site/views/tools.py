from datetime import datetime as dt


def formatDatetime(timestamp : dt) -> str:
    return timestamp.strftime("%H:%M:%S") if timestamp.date() == dt.today().date() else timestamp.strftime("%d.%m.%Y, %H:%M:%S")