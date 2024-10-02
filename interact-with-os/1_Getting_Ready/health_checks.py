#! /usr/bin/env python3
import shutil
import psutil

# du = shutil.disk_usage("/")
# print(du)

# free_percent = du.free / du.total * 100
# print(free_percent)

# print(psutil.cpu_percent(0.1))
# print(psutil.cpu_percent(0.5))


import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100

    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")
