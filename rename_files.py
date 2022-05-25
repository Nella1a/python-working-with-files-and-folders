from pathlib import Path


def main_rename():
  print("*** file: rename files in folder(files)*** \n")
  # whenever you whant to manipulate files/direc (read, delete, rename, change):

  # 1: get root-directory/folder of files
  root_dir = Path('files')

  # 2: create a path-object
  file_paths = root_dir.iterdir()
   # print(list(file_paths))

  # 3: loop over path-object, add prefix to all filenames
  prefix = input("Choose a prefix (eg: new): " )
  for path in file_paths:
    new_filename = prefix + "-" + path.stem + path.suffix
      
    #  point to correct path ("files/..") with .with_name()
    new_filepath = path.with_name(new_filename)
      
    #Path.rename(target): Rename this file or directory to the given target, and return a new Path instance pointing to target
    path.rename(new_filepath)
 
  print('\n*** Prefix succesfully added to files.\nHave a look at the folder: files.***')


