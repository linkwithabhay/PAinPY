from manipulate import terminal
import os

#$ Center the content
def centered(msg, styled, fullPage):
  size = os.get_terminal_size()
  tw = size.columns
  th = size.lines
  leftSpace = int((tw - len(msg) - 2) / 2)
  vacantSpace = int(tw * 0.2)
  w = tw - vacantSpace
  aw = w - len(msg) - 2
  h = th - 3
  topSpace = int(h / 2)
  leftStyle = int(aw / 2)
  rightStyle = aw - leftStyle
  if fullPage:
    terminal.clear()
    print("\n"*topSpace)
  if styled:
    print("{}{}".format(" "*int(vacantSpace / 2), "="*w))
    print("{}{} {} {}".format(" "*int(vacantSpace / 2), "="*leftStyle, msg, "="*rightStyle))
    print("{}{}".format(" "*int(vacantSpace / 2), "="*w))
  else:
    print(" "*leftSpace, msg)
  return


#$ Give spacing
def giveSpace(variant: str ="v" or "h" or "vh", messages: list = [""], Vspace: list = [2] or [2,2], style: bool =False, fullPage: bool = False):
  msg = ""
  if len(messages) > 0:
    for x in messages:
      if type(x) == str:
        if len(x) > 0:
          msg += x
  if variant == "v":
    print("\n"*Vspace[0])
    if len(msg) > 0:
      print(msg)
      if len(Vspace) > 1:
        print("\n"*Vspace[1])
    return
  elif variant == "h":
    if len(msg) > 0:
      centered(msg, style)
    return
  elif variant == "vh":
    if len(msg) > 0:
      centered(msg, style, fullPage)
    return
  else:
    return