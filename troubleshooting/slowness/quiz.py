import psutil

cpu_percent = psutil.cpu_percent()
print(cpu_percent)

disk_io_counters = psutil.disk_io_counters()
print(disk_io_counters)

net_io_counters = psutil.net_io_counters()
print(net_io_counters)

# Basics rsync command

# rsync(remote sync) is a utility for efficiently transferring and synchronizing files
# between a computer and an external hard drive and across networked computers by comparing the modification time and size of files.
# One of the important features of rsync is that it works on the delta transfer algorithm,
# which means it'll only sync or copy the changes from the source to the destination instead of copying the whole file.
# This ultimately reduces the amount of data sent over the network.

# rsync [Options] [Source-Files-Dir] [Destination]

# 1. Copy or sync files locally:
# rsync -zvh [Source-Files-Dir] [Destination]

# 2. Copy or sync directory locally:
# rsync -zavh [Source-Files-Dir] [Destination]

# 3. Copy files and directories recursively locally:
# rsync -zrvh [Source-Files-Dir] [Destination]

# In order to use the rsync command in Python,
# use the subprocess module by calling call methods and passing a list as an argument.

# https://www.linuxtechi.com/rsync-command-examples-linux/

import subprocess

src = "<source-path>"  # replace <source-path> with the source directory
dest = "<destination-path>"  # replace <destination-path> with the destination directory

subprocess.call(["rsync", "-arq", src, dest])

# https://realpython.com/python-concurrency/
