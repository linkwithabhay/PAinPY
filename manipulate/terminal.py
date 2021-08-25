from os import name, system
from manipulate import spacing
from time import sleep

def clear():
  # for windows
  if name == 'nt':
    _ = system('cls')
  
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')

def shutDown(code: int):
  clear()
  if code == 1:
    spacing.giveSpace("vh", ["Something is wrong. Please reinstall."],style=True ,fullPage=True)
  else:
    spacing.giveSpace("vh", ["See you soon"],style=True ,fullPage=True)
  sleep(3)
  exit(code)