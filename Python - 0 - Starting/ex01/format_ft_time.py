from datetime import datetime, date, time, timedelta
import time


seconds = time.time()

_time = time.localtime(0)

day = _time.tm_mday

formatted_time = "Seconds since " + time.strftime(f"%B {day}, %Y", _time) + ": " + f"{seconds:,.4f}" + " or " + f"{seconds:.2e}" + " in scientific notation"

print(formatted_time)

current_time = time.localtime()
current_day = current_time.tm_mday
formatted_current_time = time.strftime(f"%B {current_day}, %Y", current_time)

print(formatted_current_time)