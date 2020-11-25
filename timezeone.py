from datetime import datetime
from pytz import timezone
from zoneinfo import ZoneInfo

current_time= datetime.now()
print(current_time)

current_time_us = datetime.now()
print(current_time_us.astimezone(ZoneInfo('Europe/Amsterdam')))