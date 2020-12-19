import datetime
import time

while True:
    now = datetime.datetime.now()
    print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
    time.sleep(1)
