# Add the date when the file was created to the filenames in folder folder task_two
from pathlib import Path
from datetime import datetime

def date_created(file_path): 
  # .stat() returns an object, contains infos about the path (eg. date created in seconds from 1970/01/01)
  stats = file_path.stat()
  # get date created (in seconds)
  second_created = stats.st_ctime
  print(second_created)
  # convert seconds into readable date-format and type str
  file_created = datetime.fromtimestamp(second_created).strftime("%Y-%m-%d_%H:%M:%S")
  return file_created



def main_created_date(): 
  root_dir = Path("task_two")
  #walk through filepath
  file_path = root_dir.glob("**/*")
  for path in file_path:
    if path.is_file():
      #print(path)
      #print(path.parts)
      file_created = date_created(path)
      new_filename = file_created + "-" + path.name
      new_filepath = path.with_name(new_filename)
      path.rename(new_filepath)



