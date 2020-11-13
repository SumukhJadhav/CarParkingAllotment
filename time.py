from datetime import datetime

now = datetime.now()

current_time = now.strftime("%a %b %d %I:%M %p")

#time.strftime("%a %b %d %I:%M:%S %p %Y")

print("Current Time =", current_time)