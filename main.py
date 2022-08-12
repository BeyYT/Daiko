from daiko.engine import start, fload
import sys
from sys import exit
try:
    args = sys.argv[1]   
except:
    args = "0"

try:
    file = sys.argv[2]
except:
    file = "none"

if args == "-f":
    fload(sys.argv[2])
    exit()
if args == "-h":
    print("Daiko Arguments:\n-f <DAIKO SCRIPT FILE> | loads daiko file\n-h | help")
else:
    start()