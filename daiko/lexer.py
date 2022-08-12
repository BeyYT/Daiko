# ignore these variables
i = 0
a = {}
func = {}

#imports
import os

# Parser
def parse(text):
  # dude ignore this
  global i, a
  x = 2
  e = 1
  domaf = "b = "
  place = ""
  isinput = 0
  # print command
  if "mao" in text and "do" not in text and "braincell" not in text: # if command in text
    newtxt = text.split("mao ") # split command
    if len(newtxt) >= 2:
      while i < len(newtxt): # while number is less than length of list

        if newtxt[i] == "": # if text is blank (keyword), go to next list slot

          i = i + 1

        if newtxt[i] != "":

        # if uses var, get var
            if "gao" in newtxt[i]:
              try:
                newvar = text.split(" ")

                newvar.remove("mao")

                if len(newvar) == 2:

                  print(a[newvar[1]])
                  i = i + 1
                  return
              except:
                print("Cannot Get Non-Existent Variable.")
                return
          # else, print text
            if "buton" in text:
              if isinput == 1:
                isinput = 0
                break

              else:
                tes = input("input > ")
                print(tes)
                isinput = isinput + 1
              
            else:
              print(newtxt[1])
              i = i + 1
      if i >= len(newtxt): # once greater than or equal to, set i to 0 and return.
        i = 0
        return
    else:
      print("expected one or more arguments, got 0")
  
  # Set Variables
  if "gao" in text and "do" not in text and "braincell" not in text:
    newtxt = text.split(" ")

    if len(newtxt) == 2:
      try:
        return a[newtxt[1]]
      except:
        print("Cannot Get Non-Existent Variable.")

    if len(newtxt) == 3:
      if "buton" in newtxt[2]:
        if isinput == 1:
          isinput = 0
          return

        else:
          tes = input("input > ")
          a[newtxt[1]] = tes
          isinput = isinput + 1
      else:
        a[newtxt[1]] = newtxt[2]

    if len(newtxt) > 3:
      a[newtxt[1]] = ""

      if "maf" in newtxt[2]: # if math command in text

        newnewtxt = newtxt.copy()

        del newnewtxt[0]

        del newnewtxt[0]

        while e < len(newnewtxt):

          domaf = domaf + newnewtxt[e] + " "

          e = e + 1

        exec(domaf + "; a[newtxt[1]] = str(b)")

      while x < len(newtxt) and "maf" not in newtxt:

        a[newtxt[1]] = a[newtxt[1]] + newtxt[x] + " "

        x = x + 1

    if len(newtxt) < 2:

      print("Expected 1-2 Arguments, Got " + str(len(newtxt) - 1) + " Arguments.")

  if "do" in text: # if command in text

    newtxt = text.split(" ")

    if len(newtxt) == 2:

      ne = func[newtxt[1]]

      parse(ne)

    if len(newtxt) == 3:

      ne = func[newtxt[1]].replace("~p~", newtxt[2])

      parse(ne)

    if len(newtxt) > 3:
      fuc = newtext[1]
      del newtext
      del newtext
      del newtext

      for c in range(len(newtext)):
        place = place + newtext[c]
      
      ne = func[fuc].replace("~p~", place)
      parse(ne)

      place = ""

  if "braincell" in text and "do" not in text:
    newtxt = text.split(" ")
    print(newtxt)
    if len(newtxt) > 2:
        
        func[newtxt[1]] = ""

        while x < len(newtxt):

          func[newtxt[1]] = func[newtxt[1]] + newtxt[x] + " "

          x = x + 1
    
        x = 0
  
  if "clear" in text and "do" not in text and "braincell" not in text:

    os.system("cls")

    os.system("clear")

  if "lev" in text and "do" not in text: # if command in text

    exit(727)

  if "maf" in text and "do" not in text and "gao" not in text and "braincell" not in text: # if command in text

    newtxt = text.split(" ")

    while e < len(newtxt):

        domaf = domaf + newtxt[e] + " "

        e = e + 1

    return exec(domaf + "; print(b)")
  if "help" in text and "do" not in text and "braincell" not in text:
    print("""Daiko Help
    
mao | print command, you can give arguments such as 'mao hello!' or 'mao gao variable_name'

gao | variable storage, to get an variable, do 'gao variable', to define an variable, do 'gao variable this is an variable'

buton | user input
example: 'mao buton'

braincell | like functions, you can define an function that prints to console by doing
'braincell printhi mao hi!'
you can also use parameters by using ~p~ as a parameter placeholder.

do | executes 'braincell' function.
example: 'do print'
braincell functions with parameters are exectuted as such:
example 'do print hi!'

maf | you can do math such as 'maf 1 + 1' or 'maf 5 % 7'

if | Compares 2 values, can be numbers or strings, if values are equal, 'braincell' function will be executed
Example: 'if 1 = 1 function_name'
it can also use variables like so:
Example: 'if v-num = 1 function_name

clear | clears the console.

lev | exits daiko.""")
    
  if "if" in text and "do" not in text and "braincell" not in text:
    newtext = text.split(" ")

    value = newtext[1]

    operator = newtext[2]

    othervalue = newtext[3]

    funct = newtext[4]

    # if both values are numbers
    if "v-" in value:
      value = value.replace("v-", '')
      try:
        value = a[value]
      except:
        print("variable in first value nonexistent!")
        return
    if "v-" in othervalue:
      othervalue = othervalue.replace("v-", '')
      try:
        othervalue = a[othervalue]
      except:
        print("variable in third value nonexistent!")
        return
    if value.isnumeric() == True and othervalue.isnumeric() == True:

      if int(value) == int(othervalue) and operator == "=":
        action = func[funct]
        parse(action)
      
      else:
        return
        # leave empty
      
      if int(value) < int(othervalue) and operator == "<":
        action = func[funct]
        parse(action)
      
      else:
        return
        # leave empty
      
      if int(value) > int(othervalue) and operator == ">":
        action = func[funct]
        parse(action)
      
      else:
        return
        # leave empty


    # if values are string
    else:
      if operator == "<":
        print("how are you gonna compare a string with less than?")

      if operator == ">":
        print("how are you gonna compare a string with more than?")

      if operator == "=":

        if value == othervalue:
          action = func[funct]
          parse(action)

        else:
          return
        # leave empty