import os
from pathlib import Path

# using os module
dest_dir = os.path.join(os.getcwd(), "test_dir")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

src_file = os.path.join(os.getcwd(), "sample_data", "spider.txt")
dest_file = os.path.join(os.getcwd(), "test_dir", "spider.txt")
os.rename(src_file, dest_file)

# using pathlib module - provides an object-oriented interface to working with file systems
dest_dir = Path("./test_dir/")
if not dest_dir.exists():
    dest_dir.mkdir()

src_file = Path("./sample_data/novel.txt")
dest_file = dest_dir / "novel.txt"

src_file.rename(dest_file)
