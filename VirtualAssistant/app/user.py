from decorate import terminal
from app import storage

def askUserName():
  name = str(input("What do I call you: "))
  if not name:
    name = askUserName()
  storage.setItem("name", name)
  return name

def askUserNickName():
  terminal.clear()
  name = str(input("Should I call you 'Sensei' or something else (type 'yes' for 'Sensei' or other nickname) : "))
  if not name:
    name = askUserNickName()
  elif name == "yes":
    name = "Sensei"
  storage.setItem("nickname", name)
  return name

def preferNickName(count: int = 0):
  terminal.clear()
  if count > 0:
    prefer = str(input("Please tell me, can I call you by your nickname (type 'yes' or 'no') :  "))
  else:
    prefer = str(input("Can I call you by your nickname (type 'yes' or 'no') :  "))
  if prefer == "yes":
    prefer = True
  elif prefer == "no":
    prefer = False
  else:
    preferNickName(count + 1)
  storage.setItem("preferNickname", prefer)
  return prefer


def askMoreAboutUser():
  terminal.clear()
  print("Please tell me more about you")
  if preferNickName():
    askUserNickName()
  else:
    print("OK, I will call you by your real name")