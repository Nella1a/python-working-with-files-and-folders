# change file extension
from pathlib import Path

def main_change_extension(): 
  root_dir = Path("task_three")
  for path in root_dir.rglob("*.txt"):
    if path.is_file():
      new_filepath = path.with_suffix(".csv")
      path.rename(new_filepath)
  