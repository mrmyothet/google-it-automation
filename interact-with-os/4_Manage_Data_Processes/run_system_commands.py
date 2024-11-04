#!/usr/bin/env python3

import subprocess

# subprocess.run(["date"])
# subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "this_file_does_not_exists"])
print(result.returncode)
