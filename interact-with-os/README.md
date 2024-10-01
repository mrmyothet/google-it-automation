- [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

```bash
python -m venv .venv
source .venv/bin/activate # on Linux
pip install -r requirements.txt
```

```bash
python -m venv .venv
.\.venv\Scripts\activate # On Windows
pip install -r requirements.txt
```

Is automation worthwhile? 
```python
Time_to_automate < (time_to_perform * amount_of_times_done)
```