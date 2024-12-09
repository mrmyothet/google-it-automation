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
