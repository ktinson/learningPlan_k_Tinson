#sys.argv list that can be created with the prompt
import sys
import cowsay
if len(sys.argv) == 2:
   cowsay.cow("Hello,", sys.argv[1])
   #cowsay.trex("Hello", sys.argv[1])
else:
   print("Error")

try:
    if len(sys.argv) < 2:
     print("not enough args")
     sys.exit("Exiting with sys.exit...")
    elif len(sys.argv) > 2:
     print("too many args")
     sys.exit("Exiting with sys.exit...")

    else:
        print("Hello, my name is: ", sys.argv[1])
        print("This is the name of the program:", sys.argv[0])
        sys.exit("Exiting with sys.exit...")

except IndexError:
    print("Need argument")
    sys.exit("Exiting with sys.exit...")


