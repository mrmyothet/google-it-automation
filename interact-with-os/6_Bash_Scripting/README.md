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