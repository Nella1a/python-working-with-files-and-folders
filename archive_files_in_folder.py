# Archive files in folder
from pathlib import Path
import zipfile


def main_archive_files():
  root_dir = Path("task_five")
  for i in range(10,21):
    new_filepath = root_dir.joinpath(f'{i}.txt')
    print(new_filepath)
    new_filepath.touch()

  archiv = input("\nPress 'a' to archive files: ")
  if archiv == 'a':
    archiv_path = root_dir.joinpath('archiv.zip')
    print(archiv_path)
    with zipfile.ZipFile(archiv_path,"w") as zf:
      for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink()
    