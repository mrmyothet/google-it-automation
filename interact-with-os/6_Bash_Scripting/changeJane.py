#!/usr/bin/env python3

import sys
import subprocess

# oldFiles = sys.argv[1]
oldFiles = "./oldFiles.txt"

with open(oldFiles) as file:
    lines = file.readlines()
    for line in lines:
        old_value = line.strip()
        new_value = old_value.replace("jane", "jdoe")
        subprocess.run(["mv", old_value, new_value])
    file.close()
