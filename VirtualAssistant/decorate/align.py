from os import get_terminal_size

tw = get_terminal_size().columns

def right(msg):
  aw = tw - len(msg)
  newMsg = " "*aw + msg
  return newMsg

def center(msg):
  aw = tw - len(msg)
  left = 0
  if aw % 2 == 0:
    left = aw / 2
  else:
    left = (aw + 1) / 2
  newMsg = " "*left + msg
  return newMsg