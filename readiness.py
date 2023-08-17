#!/usr/bin/env python
import sys
import time
import psutil

PROC_NAME = "gunicorn"


def find_process(name):
    for proces in psutil.process_iter():
        if name in proces.name():
            return True

    return False


def find_process_by_command(name):
    for proces in psutil.process_iter():
        command = " ".join(proces.cmdline())
        if name in command:
            return True

    return False


if __name__ == "__main__":
    for _ in range(1000):
        if find_process(PROC_NAME):
            time.sleep(5)
            sys.exit(0)

        time.sleep(5)

    sys.exit(1)
