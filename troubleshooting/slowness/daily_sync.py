#!/usr/bin/env python3

import subprocess
from multiprocessing import Pool
import os


def run(file):
    basename = os.path.basename(file)
    print(f"Handling {basename}")

    src = os.path.join("./data/prod/", basename)
    dest = os.path.join("./data/prod_backup", basename)
    subprocess.call(["rsync", "-arq", src, dest])


src = "./data/prod/"
dest = "./data/prod_backup/"

for root, _, files in os.walk(src):
    p = Pool(len(files))
    p.map(run, files)
