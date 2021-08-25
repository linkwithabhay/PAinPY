from os import system, path
from app import storage
from manipulate import terminal, align

#! Have not given the privileges to add new DEV-ENVs to the user yet

def askOption():
  reply = int(input("Your choice: "))
  if reply == "":
    reply = askOption()
  return reply

def run_cmds(array: list):
  for value in array:
    if type(value) == list and len(value) == 2:
      if path.isabs(value[1]):
        system(value[0])
      else:
        print(f"Path '{value[1]}' does not exist!")
    else:
      system(value)

def start(errMsg: str = ""):
  '''Start a new development environment.'''
  
  terminal.clear()
  dev_env = storage.getItem("dev")
  if dev_env == Exception:
    terminal.shutDown(1)
  if errMsg:
    print(align.right(errMsg))
  if dev_env["last"] == 0:
    print("Have not started yet? Choose from the following-")
  else:
    print("Type '0' to continue where you left or")
  for i in range(1, len(dev_env)):
    name = dev_env[str(i)]["name"]
    print(f"{i}. {name}")
  reply = askOption()
  if reply == 0:
    index = dev_env["last"]
    if index == 0:
      start("No record found.")
    return run_cmds(dev_env[str(index)]["commands"])
  elif reply in range(1,i+1):
    #! Change the value of 'last' here
    return run_cmds(dev_env[str(reply)]["commands"])
  else:
    start("Wrong Input! Try Again..")
  return

if __name__ == '__main__':
  start()
