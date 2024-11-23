```bash
ls -l | less

cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

```

Redirection

```bash
./capitalize.py < haiku.txt
```

Pipe

```bash
cat haiku.txt | ./captalize.py
```

Signals

- Tokens delivered to running processes to indicate a desired action

```bash
ping www.example.com
```

```bash
ps ax | grep ping
kill 99482
```

- **mv** is used to move one or more files to a different directory, rename a file, or both at the same time.
- **cp** is used to copy one or more files
- **chmod**/**chown**/**chgrp** is used to make a file readable to everyone on the system before moving it to a public directory.
- **cut** is a command that extracts fields from a data file.
- **sort** is a command that sorts the contents of a file.
- **id** is a command that prints information about the current user.
- **free** is a command that prints information about memory on the current system.
- **free -h** This command prints in human-readable units instead of bytes.

##### Managing streams

These are the redirectors that we can use to take control of the streams of our programs

- command > file: redirects standard output, overwrites file
- command >> file: redirects standard output, appends to file
- command < file: redirects standard input from file
- command 2> file: redirects standard error to file
- command1 | command2: connects the output of command1 to the input of command2

##### Operating with processes

These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

- **ps**: lists the processes executing in the current terminal for the current user
- **ps ax**: lists all processes currently executing for all users
- **ps e**: shows the environment for the processes listed
- **kill PID**: sends the SIGTERM signal to the process identified by PID
- **fg**: causes a job that was stopped or in the background to return to the foreground
- **bg**: causes a job that was stopped to go to the background
- **jobs**: lists the jobs currently running or stopped
- **top**: shows the processes currently using the most CPU time (press "q" to quit)

In Bash scripting, an exit value of 0 means success.

Test

- A command that evaluates the conditions received and
- exits with zero when they're true
- exits with one when they're false

##### Bash Scripting Resources

- https://ryanstutorials.net/bash-scripting-tutorial/
- https://linuxconfig.org/bash-scripting-tutorial-for-beginners
- https://www.shellscript.sh/
