# Welcome to Daiko!
# This is an Engine, for some reason...
# Enjoy me having an stroke!
from daiko.inputhandle import handle
from daiko.lexer import parse
import sys 

def start():
  print("Daiko 1.0 | Running on Python " + sys.version + " | Press CTRL + C To Exit!\nStart By Typing An Command Or Typing in 'help'\n")
  handle()

def fload(file):
  if ".dk" in file:
    file1 = open(file, 'r')
    Lines = file1.readlines()
    
    count = 0
    # Strips the newline character
    for line in Lines:
      count += 1
      if "//" in line.strip():
        parse("")
      else:
        parse("{}".format(line.strip()))
  else:
    print("invalid File! please use an Daiko (.dk) file!")