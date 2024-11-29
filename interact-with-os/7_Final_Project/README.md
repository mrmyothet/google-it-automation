### Steps for coding projects

- Understand the problem statement
- Research
- Planning
- Writing

#### Introduction

Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.

### What you'll do

- Use regex to parse a log file
- Append and modify values in a dictionary
- Write to a file in CSV format
- Move files to the appropriate directory for use with the CSV->HTML converter

#### Exercise - 1

We'll be working with a log file named syslog.log, which contains logs related to ticky.

When the service runs correctly, it logs an INFO message to syslog. It then states what it did and states the username and ticket number related to the event. If the service encounters a problem, it logs an ERROR message to syslog. This error message indicates what was wrong and states the username that triggered the action that caused the problem.

In this section, we'll search and view different types of error messages. The error messages for ticky details the problems with the file with a timestamp for when each problem occurred.

These are a few kinds of listed error:

- Timeout while retrieving information
- The ticket was modified while updating
- Connection to DB failed
- Tried to add information to a closed ticket
- Permission denied while closing ticket
- Ticket doesn't exist

To grep all the logs from ticky, use the following command:

```bash
grep ticky syslog.log
```

In order to search all the ERROR logs, use the following command:

```bash
grep "ERROR" syslog.log
```

To enlist all the ERROR messages of specific kind use the below syntax.

**Syntax**: grep ERROR [message] [file-name]

```bash
grep "ERROR Tried to add information to closed ticket" syslog.log
```
