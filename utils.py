import os 
import random
from IPython.display import clear_output

def reader():
  k = int(input("k:")) 
  assert len(str(k)) > 4, "wrong format"
  k = k % 6 + 2
  clear_output()
  input_ = input("copy:")
  clear_output()
  var = ""
  for ch in input_:
    var += chr((ord(ch) - 90 - k) + 90)
  var = var.split("$#&/(#")[0]
  with open("Output.txt", "w") as text_file:
    print(f"{var}", file=text_file)
  print("Done")
  
def writer():
  k= int(input("k:"))
  assert len(str(k)) > 4, "wrong format"
  k = k % 6 + 2
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
    var += chr((ord(ch) - 90 + k) + 90)
  return var

def reset_output():
  import os
  os.remove("Output.txt")
  print("Done")
