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