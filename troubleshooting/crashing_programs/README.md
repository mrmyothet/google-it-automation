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