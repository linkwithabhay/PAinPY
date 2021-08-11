from os import error, path, getcwd
from decorate import terminal, align

def file(errMsg: str = "", dir: str = ""):
  if errMsg: print(align.right(errMsg))
  if not dir:
    dir = str(input("Enter the full path to the directory or press ENTER key for current directory:\n"))
  if dir == "":
    dir = getcwd()
  if not path.isdir(dir):
    terminal.clear()
    file("Given '{}' directory does not exist!! Try again.".format(dir))

  terminal.clear()

  print(dir)
  fileName = str(input("Enter file name with file type (like abc.py or abc.txt): "))
  filePath = ""
  filePath = path.join(dir, fileName)

  try:
    f = open(filePath, "x")
    print("{} created successfully......".format(fileName))
    f.close()
  except error:
    if error == FileExistsError:
      terminal.clear()
      file("{} already exits!".format(fileName), dir)

  return
