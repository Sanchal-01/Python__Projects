import time
from plyer import notification  # type:ignore

while True:
    print("Please sip some water !!")
    notification.notify(title = " Drink Water ",
                        message = "You need to drink some water")
    time.sleep(60*60)   # 1hr reminder
