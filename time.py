import datetime
dt_started = datetime.datetime.now()
import time
# do some stuff
print(dt_started)
time.sleep(5)

dt_ended = datetime.datetime.now()
print((dt_ended - dt_started).total_seconds())
