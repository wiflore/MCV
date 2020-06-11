import os 
import random
from IPython.display import clear_output
from datetime import datetime
import getpass


def reader():
  k = int(getpass.getpass("k: "))
  assert len(str(k)) > 4, "wrong format"
  k = k % 3 + 2
  clear_output()
  input_ = input("copy:")
  clear_output()
  var = ""
  for ch in input_:
    var += chr((ord(ch) - 5 - k) + 5)
  var = var.split("$#&/(#")[0]
  with open("Output.txt", "w") as text_file:
    print(f"{var}", file=text_file)
  print("Done")
  
def writer():
  date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
  print(f"Current date: {date}")
  k= int(getpass.getpass("k: "))
  assert len(str(k)) > 4, "wrong format"
  k = k % 3 + 2
  clear_output()
  input_ = input("Write something: ")
  clear_output()
  var = ""
  gar = "$#&/(#"
  noth = ""
  for i in range(5):
    noth+= chr(random.randint(65, 122))
  gar += noth
  input_ += gar
  for ch in input_:
    var += chr((ord(ch) - 5 + k) + 5)
  print(f"Current date: {date}")
  return var

def reset_output():
  import os
  os.remove("Output.txt")
  print("Done")
