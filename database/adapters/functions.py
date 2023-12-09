from datetime import datetime
from pytz import timezone


def datetime_local():
    return datetime.now(timezone("America/Sao_Paulo"))
