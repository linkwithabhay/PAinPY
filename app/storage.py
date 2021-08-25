import json

def getItem(at: str, keys: list = []):
  try:
    with open("app/assets/{}.json".format(at), "r") as f:
      data = json.loads(f.read())
    if not keys:
      return dict(data)
    else:
      value = ""
      for key in keys:
        if key in data.keys():
          value = data[key]
          if type(value) == dict:
            data = value
        else:
          return False
      return value
  except Exception:
    return Exception

def setItem(at: str, keys: list, value: str or dict):
  try:
    try:
      with open(f"app/assets/{at}.json", "r") as f:
        data = dict(json.loads(f.read()))

      if not len(data) or not keys[0] in data.keys() :
        raise

      if len(keys) == 2:
        data[keys[0]][keys[1]] = value

      f = open(f"app/assets/{at}.json", "w")
      json.dump(data, f, indent=2)
      f.close()
    except:
      # Executed only when file is empty or file not found
      try:
        data = {}
        obj = {}
        for index, key in enumerate(reversed(keys)):
          if index == 0:
            obj[key] = value
          else:
            obj[key] = data
          data = obj
          obj = {}
        with open(f"app/assets/{at}.json", "w") as f:
          json.dump(data, f, indent=2)
        return True
      except:
        return False
  except:
    return False

if __name__ == "__main__":
  print("0", getItem("user"))
  print("1", getItem("user", ["meta"]))
  print("2", getItem("user", ["settings","preferNickname"]))
  # print("3", setItem("us", ["data", "person", "lastName"], "Abhay"))
  # data = {"a": "A", "1": {"b": "B", "2": {"c": "C", "d": "D"}}}


## Comments
#? Single For Loop Implementation in getItem
# value = ""
# for item in items:
#   if item in data.keys():
#     value = data[item]
#     if type(value) == dict:
#       data = value
#   else:
#     return False
# return value

#? Double For Loop Implementation in getItem
# search = data
# for index, item in enumerate(items):
#   for key, value in search.items():
#     if key == item and index == len(items) - 1:
#       return value
#   search = search[item]
# return None