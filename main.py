import pywhatkit
from datetime import datetime, timedelta
import time


def main():
    for _ in range(50):
        now = datetime.now() + timedelta(minutes=2)
        time.sleep(5)
        current_hour = now.strftime("%H")
        current_month = now.strftime("%M")
        print("current hour is {} and month is {}".format(current_hour, current_month))
        pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "Hello, How are you!!", int(current_hour), int(current_month))


if __name__ == "__main__":
    main()
