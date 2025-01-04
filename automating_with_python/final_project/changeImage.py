#!/usr/bin/env python3

import os
from PIL import Image

root_path = os.getcwd()
folder_path = os.path.join(root_path, "supplier-data/images")

for filename in os.listdir(folder_path):
    print(filename)
