#!/usr/bin/env python3

import subprocess

# from multiprocessing import Pool
import os
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm


def progress_bar(files):
    return tqdm(files, desc="Processing", total=len(files), dynamic_ncols=True)


def run(root, basename):
    filename = f"{root}/{basename}"
    print(f"Handling {filename}")

    src = filename
    dest = os.path.join(os.getcwd() + "/data/prod_backup/", basename)

    print(f"Source: {src}")
    print(f"Destination: {dest}")

    subprocess.call(["rsync", "-arq", src, dest])


src = os.getcwd() + "/data/prod/"
dest = os.getcwd() + "/data/prod_backup/"

executor = ProcessPoolExecutor()

for root, dirnames, filenames in os.walk(src):
    for basename in progress_bar(filenames):

        if len(filenames) == 0:
            continue

        print(root)
        # print(dirnames)
        print(filenames)

        # p = Pool(len(filenames))
        # p.map(run, root, filenames)

        executor.submit(run, root, basename)
print("Waiting for all threads to finish....")
executor.shutdown()
