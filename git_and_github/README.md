```bash

cp disk_usage.py disk_usage_original.py
cp disk_usage.py disk_usage_fixed.py

# make changes - fixed
# generate diff

diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diff

# patch diff file
patch disk_usage.py < disk_usage.diff

```

```bash
git config -l
git config list
```