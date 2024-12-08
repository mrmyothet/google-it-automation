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
