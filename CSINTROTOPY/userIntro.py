
users = []
names = input("Enter name: ")
for i in range(3):
    users.append(input("User: "))
for name in sorted(users):
    print(f'Hello, {name}')
    
with open("names.txt", "a") as filename:
    filename.write(f'{names}\n')
    for name in sorted(users, reverse=True):
        filename.write(f'{name}\n')
filename.close()
with open("names.txt", "r") as filename:
    for line in filename:
        print("hello, ", line.rstrip())