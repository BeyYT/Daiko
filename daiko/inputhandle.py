from daiko.lexer import parse

def handle():
  while True:
    enter = input("> ")
    parse(enter)
  