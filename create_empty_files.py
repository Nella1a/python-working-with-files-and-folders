# create empty files
from pathlib import Path
import os

    
def remove_files(root_dir):
  for path in os.listdir(root_dir):
    os.remove(os.path.join(root_dir,path))


def main_empty_files():
  root_dir = Path("task_four")
  for i in range(10,21):
    filepath = root_dir.joinpath(f'{i}.txt')
    filepath.touch()

  user_input = input("Files successfully added to folder: task_four.\nPress 'r' to delete all files.\n>> ")
  if user_input == "r":
    remove_files(root_dir)
                       
  

