# ---String manipulation
print("Hello World") 
newMessage = "week9: Python Basics"
print(newMessage)
# ----Built in methods
print(newMessage.capitalize())
print(newMessage.upper())
revMes = reversed(newMessage)
# --without the list it just says an object was created
listMes =list(revMes)
print(listMes)
print(newMessage.strip(" "))
print(newMessage.swapcase())
pyslice = slice(6)
print(newMessage[pyslice])
num = 111
# ----Wrappers
print(str(num) + " "+ newMessage)
# ------User input
language = input("Testing for basics:")
print("learning: " + language)