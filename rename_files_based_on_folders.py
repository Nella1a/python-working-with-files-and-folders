from pathlib import Path


def main_rename_folder(): 
  print("Rename filenames by adding the name of the folder to the filename (eg. December-ghi.txt)\n ")

 # first option 
  '''
  root_dir = Path("folders")
  file_path = root_dir.iterdir()
  for path in file_path:   
    for file in path.iterdir:
      file_name = f'{path.name}-{file.name}'
      print("fileName", file_name)
      file_path = file.with_name(file_name)
      print("filePath:",file_path)
      file.rename(file_path)
      #print(file.name)
  '''


    
