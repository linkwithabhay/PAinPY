from manipulate import spacing, terminal
from commands import create, dev
from app import storage, user
from app.voice_assistant import Voice_Assistant
from time import sleep

#$ ======================= Functions =======================


#$ Greet User
def greet(name: str, firstTime: bool):
  terminal.clear()
  if firstTime:
    spacing.giveSpace("vh", ["Welcome {}".format(name)],style=True ,fullPage=True)
  else:
    spacing.giveSpace("vh", ["Welcome back {}".format(name)],style=True ,fullPage=True)
  sleep(3)
  terminal.clear()


#$ Assistant
def Assistant():
  what = str(input("What do you want to do now (type 'help' to know more) : "))
  if what == "help":
    return listOfCommands()
  elif what == "create":
    return create.file()
  elif what == "dev":
    return dev.start()
  elif what == "rs":
    return start()
  elif what == "close":
    return terminal.shutDown(0)
  elif what == "profile":
    return user.showProfile()
  elif what == "":
    return Assistant()
  else:
    print("'{}' command is not understandable by me.".format(what))
    return Assistant()


#$ List of available commands
def listOfCommands():
  terminal.clear()
  commands = storage.getItem("commands")
  if not commands:
    return terminal.shutDown(1)
  print("-"*20, "Available Commands", "-"*20)
  spacing.giveSpace("v",Vspace=[0])
  longst = commands["meta"]["longest"]
  for key,value in commands["commands"].items():
    print(value["name"], " "*((longst - len(value["name"])) + 5), value["des"])
  spacing.giveSpace("v")
  return Assistant()


#$ =================== Start from here ===================
def start():
  firstTime = False
  callByNickname = storage.getItem("user", ["settings","preferNickname"])
  if callByNickname == None:
    user.askMoreAboutUser()
    start()
  elif callByNickname is True:
    name = storage.getItem("user", ["data","nickname"])
  else:
    name = storage.getItem("user", ["data","name"])
  if not name:
    name = user.askUserName()
    firstTime = True
  greet(name, firstTime)
  if firstTime:
    user.askMoreAboutUser()
  Assistant()

if __name__ == "__main__":
  # start()
  Voice_Assistant()