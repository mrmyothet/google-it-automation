# The data inside dictionaries take the form of
# pairs of keys and values

x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

txt_count = file_counts["txt"]
print("txt file count", txt_count)

is_there_jpg = "jpg" in file_counts
is_there_html = "html" in file_counts
print("Is there jpg files ", is_there_jpg)
print("Is there html files ", is_there_html)

file_counts["cfg"] = 8
print(file_counts)

file_counts["csv"] = 17
print(file_counts)

del file_counts["cfg"]
print(file_counts)
