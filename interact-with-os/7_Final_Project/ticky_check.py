#!/usr/bin/env python3

import re
import operator
import csv

errors = {}
per_user = {}

with open("./syslog.log", "r") as log:
    lines = log.readlines()
    for line in lines:
        match = re.search(r"ticky: INFO ([\w ]*)\[#\d+\] (\(\w*\))", line)
        if match:
            # print(match[1], match[2])
            error_message = match[1]
            user_name = match[2]
            user_name = user_name[1:]
            user_name = user_name[:-1]
            per_user[user_name] = per_user.get(user_name, 0) + 1

        match = re.search(r"ticky: ERROR ([\w ]*)(\(\w*\))", line)
        if match:
            # print(match[1], match[2])
            error_message = match[1]
            user_name = match[2]
            errors[error_message] = errors.get(error_message, 0) + 1
log.close()


errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items(), key=operator.itemgetter(0))

per_user.insert(0, ("Username", "INFO", "ERROR"))
errors.insert(0, ("Error", "Count"))

print(errors)
print(per_user)

with open("error_message.csv", "w") as error_message_csv:
    writer = csv.writer(error_message_csv)
    writer.writerows(errors)

with open("user_statistics.csv", "w") as user_stat_csv:
    writer = csv.writer(user_stat_csv)
    writer.writerows(per_user)
