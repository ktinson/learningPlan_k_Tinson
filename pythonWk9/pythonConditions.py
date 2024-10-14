newAge = input("What is your age? ")
age = int(newAge)
if age > 95:
    print("You've been here some time.")
elif age <= 94 and age >= 52:
    print("You're a senior citizen.")
elif 18 <= age <=51:
    print("We work.")
elif age < 18:
    print("Youth")
print("Done")