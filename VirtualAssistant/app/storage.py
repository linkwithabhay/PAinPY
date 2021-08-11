import json

def getItem(item: str):
  try:
    f = open("VirtualAssistant/app/assets/user.json", "r")
    data = json.loads(f.read())
    f.close()
    for key, value in data.items():
      if key == item:
        return value
    return False
  except Exception:
    return False

def setItem(key: str, value: str or dict):
  try:
    try:
      f = open("VirtualAssistant/app/assets/user.json", "r")
      data = json.loads(f.read())
      f.close()
      found = False
      for ky in data.keys():
        if ky == key:
          data[key] = value
          found = True
          break
      if not found:
        data[key] = value
      f = open("VirtualAssistant/app/assets/user.json", "w")
      json.dump(data, f, indent=2)
      f.close()
    except:
      data = {}
      data[key] = value
      f = open("VirtualAssistant/app/assets/user.json", "w")
      json.dump(data, f, indent=2)
      f.close()
    return True
  except:
    return False