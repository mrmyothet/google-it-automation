with open("sample_data/novel.txt", "w") as file:
    file.write("It was a dark and stormy night.")

with open("sample_data/novel.txt", "r+", encoding="utf-8") as requirements:
    print(requirements.read())
