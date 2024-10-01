import os

os.remove("sample_data/novel.txt")
# os.remove("sample_data/novel.txt")  # FileNotFoundError

os.rename("first_draft.txt", "finished_master_piece.txt")

print(os.path.exists("finished_master_piece.txt"))
print(os.path.exists("user_list.txt"))
