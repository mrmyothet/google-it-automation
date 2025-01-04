#! /usr/bin/env python3

import os
import requests

root_path = os.getcwd()
folder_path = os.path.join(root_path, "supplier-data/descriptions")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r") as file:
        lines = file.readlines()
        # print(lines)
        name = lines[0]
        weight = lines[1]
        description = lines[2]
        print(name, weight, description)
