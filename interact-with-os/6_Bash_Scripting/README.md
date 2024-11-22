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