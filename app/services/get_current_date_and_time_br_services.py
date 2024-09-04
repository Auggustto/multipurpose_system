from datetime import datetime
import pytz

def get_current_time():
    tz = pytz.timezone('UTC')
    return datetime.now(tz)


def format_datetime(dt):
    local_tz = pytz.timezone('America/Sao_Paulo')
    local_dt = dt.astimezone(local_tz)
    return local_dt.strftime("%d/%m/%Y %H:%M:%S")