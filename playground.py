# playground.py

import constants
import time
from datetime import datetime


i = 0
while i < 3:
    i += 1
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8) < datetime.now() < \
            datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16):
        print('working hours...', datetime.now())
        time.sleep(1)

        with open(constants.hosts, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            if not any(website in row for row in f for website in constants.blocked_websites):
                # if here -> the file doesn't contain any blocked_websites
                for website in constants.blocked_websites:
                    # append '127.0.0.1' IP address and each blocked_website
                    f.write('127.0.0.1' + '\t' + website + '\n')

    else:
        print('fun hours...', datetime.now())
        time.sleep(1)
        with open(constants.hosts, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for row in content:
                if not any(website in row for website in constants.blocked_websites):
                    # if here -> the row doesn't contain any blocked_websites
                    f.write(row)
            # reached the end of 'content', but not the end of f
            # must remove everything from this point in f(e.g.: the blocked_websites)
            f.truncate()

with open(constants.hosts) as f:
    for row in f:
        print(row)