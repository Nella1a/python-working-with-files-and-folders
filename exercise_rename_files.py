from pathlib import Path

def main_exercise_rename():
  root_dir = Path('task_one')  
  #walk through filepath
  for path in root_dir.glob("**/*"):
    # check if item is a file
    if path.is_file():
      #print(path)
      year = path.parts[-3]
      month = path.parts[-2]
      #print(year, month, path.name)
      new_filename = f'{year}-{month}-{path.name}'
      new_filepath = path.with_name(new_filename)
      #print(new_filepath)
      path.rename(new_filepath)
      

     