import os

def start():
  chrome_path = "\"C:\Program Files\Google\Chrome\Application\chrome.exe\" -incognito"
  url = "http://localhost:3000"
  print(chrome_path, url)
  os.system(chrome_path + " " + url)
  return

  # clientPath = "C:\\Web Dev\\Github\\ToDo App\\todo-app-client"
  # serverPath = "C:\\Web Dev\\Github\\ToDo App\\todo-app-server"
  # codePath = "\"C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" -n"
  # os.system(codePath + " " + clientPath)
  # os.system(codePath + " " + serverPath)