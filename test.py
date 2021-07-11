# import sys
# print (sys.argv)

# import os
# os.system("python3 --version")

# stream = os.popen('echo Returned output')
# output = stream.read()
# print(output)

# s = "python3 --version"
# type(s)
# os._wrap_close
# for e in s:
#     print(e, end='')

import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    file = None