import json

def get():
  try:
    f = open("app/assets/commands.json", "r")
    data = json.loads(f.read())
    f.close()
    return data
  except:
    return False