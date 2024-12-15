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

### Resources for understanding crashes

-[Why do computers crash?](https://www.scientificamerican.com/article/why-do-computers-crash/)

- [PC Guide - sitemap](https://www.pcguide.com/sitemap/)
- [how to find crash logs, error logs on Windows 10](https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/)
- [How to View the System Log on a Mac](https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/)
- [How to Check System Logs on Linux](https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm)
- [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [Linux strace Command](https://www.howtoforge.com/linux-strace-command/)
- [Tracing System calls](https://neurocline.github.io/dev/2015/05/24/Tracing-System-Calls.html)
