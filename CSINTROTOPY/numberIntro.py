

try:
    x = int(input("What's x : "))
except ValueError:
    print("x is not an interger")
else:
    print(f'x is {x}')