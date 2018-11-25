# playground.py

import constants
import time
from datetime import datetime


i = 0
while i <= 5:
    i += 1
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8) < datetime.now() < \
            datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16):
        print('working hours...', datetime.now())
        time.sleep(1)

        with open(constants.hosts, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            if not any(website in row for row in f for website in constants.blocked_websites):
                for website in constants.blocked_websites:
                    f.write('127.0.0.1' + '\t' + website + '\n')

    else:
        print('fun hours...')


with open(constants.hosts) as f:
    for row in f:
        print(row)