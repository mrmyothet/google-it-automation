#!/usr/bin/env python3

import os
from PIL import Image

root_path = os.getcwd()
folder_path = os.path.join(root_path, "supplier-data/images")

for filename in os.listdir(folder_path):
    # print(filename)
    if filename == "LICENSE" or filename == "README":
        continue
    img = Image.open(os.path.join(folder_path, filename))
    # print(img.filename, img.format, img.size)
    new_img = img.resize((600, 400)).convert("RGB")

    new_filename = os.path.join(folder_path, filename.split(".")[0] + ".jpeg")
    print(new_filename)
    new_img.save(new_filename)
    img.close()
