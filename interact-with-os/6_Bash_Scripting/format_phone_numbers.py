import re

with open("./data/phones.csv", "r") as file:
    phones = file.readlines()

    for phone in phones:
        old_phone = phone.strip()
        new_phone = re.sub(r"^\D*(\d{3})\D*(\d{3})\D*(\d{4})$", r"(\1) \2-\3", phone)
        print(new_phone)
