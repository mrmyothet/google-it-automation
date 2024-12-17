# Troubleshooting and Debugging Techniques

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

### Terms and definitions (concepts)

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

### Expensive Loops

- read file, read data over the network before the loops
- break out of the loops once you've found what you were looking for.

---

real 0m0.129s
user 0m0.068s
sys 0m0.013s

- **real** The amount of actual time that it took to execute the command
- **user** The time spent doing operations in the user space
- **sys** The time spent doing system-level opertions

```bash
sudo apt-get install python3-pprofile
sudo snap install kcachegrind
```

```bash
pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1, test2, test3, test4, test5, test6, test7, test8, test9"

kcachegrind profile.out
```

```bash
pip install pprofile

pprofile -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1, test2, test3, test4, test5, test6, test7, test8, test9"

brew install qcachegrind
```

---

**Threads** Let us run parallel tasks inside a process.
**Executor** The process that's in charge of distributing the work among the different workers.
**Futures** module - Provides a couple of different executors; one for using threads and another for using processes.

---

### [concurrency and parallelism](https://realpython.com/python-concurrency/)

### [Asyncio events and task loops](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)

---

### Terms and definitions (slowness)

- **Activity Monitor:** Mac OS tool that shows what's using the most CPU, memory, energy, disk, or network
- **Resource Monitor (or Performance Monitor):** Windows OS tool that shows what's using the most CPU, memory, energy, disk, or network
- **Cache:** This stores data in a form that's faster to access than its original form
- **Executor:** This is the process that's in charge of distributing the work among the different workers
- **Expensive actions:** Actions that can take a long time to complete
- **Futures:** A module provides a couple of different executors, one for using threads and the other one for using processes
- **Lists:** Sequences of elements
- **Memory leak:** This happens when a chunk of memory that's no longer needed is not released
- **Profiler:** A tool that measures the resources the code is using to see how the memory is allocated and how the time is spent
- **Threads:** Run parallel tasks inside a process
- **Real time:** The amount of actual time that it took to execute the command
- **Sys time:** The time spent doing system level operations
- **User time:** The time spent doing operations in the user space

---

## Crashing Programs

### Why Programs Crash

**Wrapper:** A function or program that provides a compatibility layer between two functions or programs,
so they can work well together.

**Watchdog** A process that checks whether a program is running and, when it's not, starts the program again

**Reproduction case**

- What were you trying to do?
- What were the steps you followed?
- What did you expect to happen?
- What was the actual outcome?

```bash
date

cd /var/log

ls -lt | head

tail syslog

sudo netstat -nlp | grep :80

ls -l /etc/nginx/

ls -l /etc/nginx/sites-enabled

vim /etc/nginx/sites-enabled/site.example.com.conf

ls -l /etc/uwsgi/

sudo service uwsgi reload

sudo chown www-data.www-data site.log

```

### Code that Crashes

- **Traceback** shows the lines of the different functions that were being executed when the problem happened.
- **Off-by-one-error**

Debugging C programs

```bash
# generate core file
ulimit -c unlimited

ls -l core

gdb -c core example

backtrace

list

up

```

---

```bash
pdb3 update_products.py --filename new_products.csv
(Pdb) continue
(Pdb) print(row)
(Pdb) exit()
```

---

### Real-world code examples

- [Minecraft](https://github.com/fogleman/Minecraft)
- [CherryPy web framework](https://github.com/cherrypy/cherrypy)
- [Flask web application framework](https://github.com/pallets/flask)
- [Tornado web framework](https://github.com/tornadoweb/tornado)
- [Howdoi command line tool](https://github.com/gleitz/howdoi)
- [Bottle web framework](https://github.com/bottlepy/bottle/blob/master/bottle.py)
- [SQLAlchemy database toolkit](https://github.com/sqlalchemy/sqlalchemy)
- [Complete Application - Home Assistant](https://github.com/home-assistant/core)

---

### Communication and Documentation

**Communications lead:**
Needs to know what's going on,
and provide timely updates on the current state
and how long until the problem's resolved.

- The root cause
- How you diagnosed the problem and found that root cause
- What you did to fix the issue
- What needs to be done to prevent the problem from happening again

**Postmortems:** Documents that describe details of incidents to help us learn from our mistakes.

- what happened
- why it happened
- how it was diagnosed
- how it was fixed
- how to prevent the same event happening in the future

---

- what caused the issue
- what the impact of the issue was
- how it got diagnosed
- the short-term remediation you applied
- the logn-term remediation you recommend
- lessons learned

---

### Terms and definitions - (crashing programs)

- **Breakpoints:** Debugging features that lets code run until a certain line of code is executed
- **Communications lead:** The lead person who needs to receive timely important communication updates
- **Core files:** Files that store all the information related to the crash to debug the issue
- **Incident commander (incident controller):** The person who needs to look at the big picture and decide what's the best use of the available resources
- **Pointers:** The variables that store memory addresses
- **Postmortems:** Documents that describe details of incidents to learn from mistakes
- **Undefined behavior:** The code is doing something that's not valid in that programming language
- **Valgrind:** A powerful tool that can tell if the code is doing any invalid operations, no matter if it crashes or not
- **Watchdog:** This is another process that checks whether a program is running and, when it's not, starts the program again
- **Watchpoints:** Debugging feature that lets code run until a variable or expression changes
- **Wrapper:** A function or program that provides a compatibility layer between two functions or programs, so that

---

### Qwiklabs assessment: Fix errors in Python scripts

**Matplotlib** is a plotting library for the Python programming language
and its numerical mathematics extension NumPy(installed upon installing matplotlib).
It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits.
Even simpler, it's a visualization library in Python for 2D plots of arrays.

---

```bash
pip install memory_profiler

python3 -m memory_profiler update_products.py

```

```bash
sudo lsof | grep deleted
```

---

**Latency:** The delay between sending a byte of data from one point and receiving it on the other
**Bandwidth:** How much data can be sent or received in a second

---

```bash
od -cx /dev/urandom

top
```

top columns

- **RES** - dynamic memory preserved for the specific process
- **SHR** - memory that's shared across processes
- **VIRT** - virtual memory allocated for each process

---

**Decorator:** Used in Python to add extra behavior to functions without having to modify the code

---

### Managing Our Time

1. Make a list of all the tasks that need to get done
2. Check the real urgency of the tasks
3. Assess the importance of each issue
4. How much effor they'll take

- [The “Everything is Important” paradox: 9 practical methods for how to prioritize your work (and time)](https://blog.rescuetime.com/how-to-prioritize/)

---

### Change management in virtualized environments

- [Best practices for Compute Engine disk snapshots](https://cloud.google.com/compute/docs/disks/snapshot-best-practices)
- [Restore from a snapshot](https://cloud.google.com/compute/docs/disks/restore-snapshot)
- [Create archive and standard disk snapshots](https://cloud.google.com/compute/docs/disks/create-snapshots)
- [Create schedules for disk snapshots](https://cloud.google.com/compute/docs/disks/scheduled-snapshots)
- [Using Snapshots To Manage Virtual Machines](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html)

---

### Containerized Applications: Docker

- [Use containers to Build, Share and Run your applications](https://www.docker.com/resources/what-container/)
- [Containerized Applications Overview](https://www.datadoghq.com/knowledge-center/containerized-applications/)
- [How To Install WordPress With Docker Compose](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-docker-compose)
- https://docker-curriculum.com/
- https://www.docker.com/101-tutorial/
- [6 Docker Alternatives to Look Out for in 2024](https://jfrog.com/devops-tools/article/alternatives-to-docker)
- [Docker vs. Containerd: A Quick Comparison (2023)](https://kodekloud.com/blog/docker-vs-containerd/)

---

### Preventing future breakage

- [What Could Possibly Go Wrong?](https://deploy.equinix.com/blog/explaining-failure-domains-sre-lifeblood/)
- [How to Solve Coding Problems with a Simple Four Step Method](https://www.freecodecamp.org/news/how-to-solve-coding-problems)
- [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)

---

### Terms and definitions (Managing Resources)

- **Bandwidth:** How much data can be sent or received in a second
- **Centralized logs collection:** This means there's a special server that gathers all the logs from all the servers, or even all computers in the network
- **Decorator:** Used in Python to add extra behavior to functions without having to modify the code
- **Exhausted:** When resources are used completely and programs are getting blocked by not having more access to those resources
- **Garbage collector:** A tool in charge of freeing the memory that's no longer in use
- **Latency:** The delay between sending a byte of data from one point and receiving it on the other
- **Memory profiler:** A tool used to figure out how the memory is being used
- **Reproduction case:** A clear description of how and when the problem appears, a way to verify if the problem is present or not
- **Swap:** A space in the hard drive where the operating system puts the parts of the memory that aren't currently in use
- **Technical debt:** The pending work that accumulates when a quick-and-easy solution is applied instead of a sustainable long-term one
- **Traffic shaping:** This is a way of marking the data packets sent over the network with different priorities, to avoid having huge chunks of data use all of the bandwidth
