#sys.argv list that can be created with the prompt
import sys
try:
    if len(sys.argv) < 2:
     print("not enough args")
    elif len(sys.argv) > 2:
     print("too many args")
    else:
        print("Hello, my name is: ", sys.argv[1])
        print("This is the name of the program:", sys.argv[0])
except IndexError:
    print("Need argument")

