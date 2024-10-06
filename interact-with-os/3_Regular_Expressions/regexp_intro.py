import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
last_index = log.index("]")
print(log[index + 1 : last_index])

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result)
print(result[0])
print(result[1])
