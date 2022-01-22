from subprocess import call
from driver import *
from datetime import datetime as dt
import vars

# Check if day has classes in the morning
today = dt.today().weekday()

if today in [0, 3, 4]:
    # Start Teams app and waits for 10 seconds to load before proceeding
    today = dt.today().strftime("%A")
    print(f"Opening first class for {today}...")
    call([vars.PATH, "--processStart", "Teams.exe"])
    sleep(15)
    driveToClass(today)
else:
    print("No class found")
    exit(1)