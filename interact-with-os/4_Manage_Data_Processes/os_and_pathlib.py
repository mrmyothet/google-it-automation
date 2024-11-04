import os
from pathlib import Path
import subprocess

cwd_subprocess = subprocess.check_output(
    [
        "pwd",
    ],
    text=True,
).strip()
print(cwd_subprocess)

cwd_os = os.getcwd()
print(cwd_os)

cwd_pathlib = Path.cwd()
print(cwd_pathlib)

subprocess.run(["mkdir", "test_dir_subprocess"])

os.mkdir("test_dir_os")

test_dir_pathlib = Path("test_dir_pathlib")
test_dir_pathlib.mkdir(exist_ok=True)
