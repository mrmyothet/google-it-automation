Whenever possible, we should check our hypothesis in a test environment,
indead of the production server that our users are working with.

```bash
sudo apt-get install iotop
sudo iotop
```

other related tools

```bash
iostat
vmstat
```

then

```bash
ionice
```

```bash
sudo apt-get install iftop
sudo iftop
```

Limit the bandwidth

```bash
rsync -bwlimit
```

### Heisenbugs

Turning Off and On again (Reboot or restart a program)

- releasing all allocated memory
- deleting temporary files
- resetting running state of programs
- re-establishing network connection
- closing opened files

---

SMTP - Failure to send email: [Errno 111] Connection refused

```bash
sudo apt install net-tools
netstat -nlt | grep '\<\25>'
```

- [aiosmtpd](https://aiosmtpd.aio-libs.org/en/latest/cli.html)

```bash
pip install aiosmtpd
python3 -m aiosmtpd -n
```

```bash
telnet localhost 8025
```

---

### Bisect Method

```bash
cat contacts.csv | ./import.py --server test
# Import error
wc -l contacts.csv
# 100 contacts.csv
head -15 contacts.csv
tail -20 contacts.csv
head -50 contacts.csv | ./import.py --server test
# Import error
head -50 contacts.csv | head -25 | ./import.py --server test
# Import successful
head -50 contacts.csv | tail -25 | ./import.py --server test
# Import error
head -50 contacts.csv | tail -25 | head -13 | ./import.py --server test
# Import successful
head -50 contacts.csv | tail -25 | tail -12 | head -6 | ./import.py --server test
# Import error
head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3 | ./import.py --server test
# Import error
```

---

### Terms and definitions

- **Binary search:** A search algorithm used to find a specific item in a sorted list or array by repeatedly dividing the search space in half until the desired item is found or determined to be absent
- **Bisecting:** Dividing in two, also a Git command
- **Debuggers:** Tools that follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more
- **Debugging:** The process of identifying, analyzing, and removing bugs in the actual code of a system in the application
- **Linear search:** The process of searching each line of data until the desired data entry is located
- **Observer effect:** The idea that observing a phenomenon alters the phenomenon
- **System calls:** The calls that the programs running on our computer make to the running kernel
- **Troubleshooting:** The process of solving any kind of problem in the system running the application

---

```bash
logrotate
```

Apache Benchmark

```
sudo apt-get install apache2-utils
```

```bash
ab -n 500 site.example.com
```

```bash
top

nice

renice

for pid in $(pidof ffmpeg); do renice 19 $pid; done

ab -n 500 site.example.com

ps ax | less

locate static/001.webm

grep ffmpeg *

killall -STOP ffmpeg

for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done;

ab -n 500 site.example.com
```

### Windows processes

Windows Process Monitor, also known as Sysinternals, is a powerful monitoring tool that serves as an advanced task manager.  
It provides real-time insight into various aspects of the system, including file system operations, registry changes, processes, and threads.  
The tool excels at diagnosing file access issues, analyzing system configurations, and understanding processes.

- https://learn.microsoft.com/en-us/sysinternals/downloads/procmon

### Linux performance

To enhance your Linux system's performance, you can use specialized tools  
that offer real-time insights into CPU, memory, disk I/O, and network activity for quick performance bottleneck detection.
Some of these tools include **Perf-tools**, **bcc/BPF**, and **bpftrace**.

- https://www.brendangregg.com/linuxperf.html

### The USE method

The USE Method is essential for optimizing system performance and troubleshooting servers.  
It helps identify resource bottlenecks and performance issues by analyzing Utilization, Saturation, and Errors.
Resources like CPUs, memory, storage, and network interfaces can be measured for busy time, additional workload capacity, and errors.

- https://brendangregg.com/usemethod.html

---

- [macOS Activity Monitor](https://support.apple.com/guide/activity-monitor/welcome/mac)
- [Windows Performance Monitor](https://www.windowscentral.com/how-use-performance-monitor-windows-10)
- [Windows Resource Monitor](https://www.digitalcitizen.life/how-use-resource-monitor-windows-7/)
- [Windows Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)

---

### Writing efficient code 

We should always start by writing clear code that does what it should, 
and only try to make it faster if we realize that it's not fast enough.

- **Profiler:** A tool that measures the resources that our code is using, giving us a better understanding of what's going on
- **gprof** for C programs
- **cProfile module** for Python programs

**Expensive actions** Those that can take a long time to complete

---

### Using the right data structures 

**Lists** 
Sequences of elements. 
We can add, remove or modify the elements in them,
and we can iterate through the whole list to operate on each of the elements.

- List in Python
- ArrayList in Java
- Vector in C++
- Array in Ruby
- Slice in Go

**Dictionaries**
Store key-value pairs.
We add data by associating a value to a key. 
and then we retrive a value by looking up a specific key.

- Dictionary in Python
- HashMap in Java
- Unordered Map in C++
- Hash in Ruby
- Map in Go

If we need to access elements by position, or 
will always iterate through all the elements, use a list to store them.
- list of computers in the network
- employees in the company
- products curently on sales

If we need to look up the elements using a key, we will use a dictionary.
- user associated by user name
- IP associated by host name 
- data associated by product code 

---