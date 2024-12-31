from PIL import Image
import os

root_path = os.getcwd()
folder_path = os.path.join(root_path, "images")

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        print(filename)
        img = Image.open(os.path.join(folder_path, filename))
        print("Name:", filename, "Format:", img.format, "Size:", img.size)

        new_img = img.rotate(90).resize((128, 128)).convert("RGB")

        new_filename = os.path.join(root_path, "result_images", filename + ".jpeg")
        print("Name:", new_filename, "Format:", new_img.format, "Size:", new_img.size)
        new_img.save(new_filename)
