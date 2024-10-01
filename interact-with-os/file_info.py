#! /usr/bin/env python3
import os
import datetime

file_size = os.path.getsize("sample_data/spider.txt")
print(file_size)

timestamp = os.path.getmtime("sample_data/spider.txt")
print(timestamp)

date_time = datetime.datetime.fromtimestamp(timestamp)
print(date_time)

absolute_path = os.path.abspath("sample_data/spider.txt")
print(absolute_path)

file = "guests.txt"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print(os.path.getsize(file))
