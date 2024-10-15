import re
email = input("Enter Email: ").strip()
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
try:
    #. 0 or more characters  before the @
    #any character except an at [^@] so @ can only appear once
    #[]set of characters [^] complimenting a set make it the opposite
    #if re.search(r"^[^@]+@[^@]+\.edu$", email):
    #if re.search(r"^[a-zA-Z09_]-+@[a-zA-Z09_]+\.edu$", email):
    #\w any word char including numbers and _
    #if re.search(r"^\w+@(\w\.)?\w+\.(edu$|com$)", email, re.IGNORECASE):
    if re.search(regex, email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    print("EROROROROROROROR")