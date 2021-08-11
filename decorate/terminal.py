from os import name, system
from decorate import spacing
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
  spacing.giveSpace("vh", ["See you soon"],style=True ,fullPage=True)
  sleep(3)
  clear()
  exit(code)