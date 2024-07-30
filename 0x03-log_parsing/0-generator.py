#!/usr/bin/python3
"""
Log Parsing
"""
import random
import sys
from time import sleep
import datetime


for i in range(10000):
    sleep(random.random())
    now = datetime.datetime.now()
    ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    status = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    size = random.randint(1, 1024)

    log_line = (
        f"{ip} - [{now}] "
        f"\"GET /projects/260 HTTP/1.1\" {status} {size}\n"
    )
    sys.stdout.write(log_line)
    sys.stdout.flush()
