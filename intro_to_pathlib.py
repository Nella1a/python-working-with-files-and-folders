from pathlib import Path


def main_pathlib(): 
  print("*** file: intro to pathlib ***\n")
  #### path to a file #####
  p1 = Path('files/ghi.txt')
  print(type(p1))
  
  if not p1.exists(): 
    with open(p1,"w") as file:
     file.write("content 3")
  
  
  # get full file name
  print(p1.name)
  
  # get file name without extension
  print(p1.stem)
  
  # get only file extension
  print(p1.suffix)
  
  #### path to folder / directory ####
  f1 = Path('files')
  for file in f1.iterdir():
    print(file)