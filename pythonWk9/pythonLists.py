names =  ["Olivia", "Liam", "Emma", "Noah", "Ava", "Oliver", "Sophia", "Elijah", "Amelia", "James"]
print(names[0], names[-2], names[5], names[6:9])
print(f'names[0] = {names[0]}, names[-2] = {names[-2]}, names[5] = {names[5]}, names[6:9] = {names[6:9]}')
print(names)
print(list(reversed(names)))
print(" ".join(names))
numbers = [1, 33, 67, 5]
print(numbers)
numbers.append(int(input("Add a number to the list: ")))
print(numbers)
print(33 in numbers)
print("Olivia" in names)
names.insert(-4, "Monikai")
print(names)
for item in numbers:
    print(item)
m = 0
while m < len(numbers):
    print(f'{m} : {numbers[m]}')
    m += 1
p = 0
while p < len(names):
    print(f'{p} : {names[p]}')
    p += 1

rangedNum = range(11)
for num in rangedNum:
    print(f'rangedNum(11){num}')
for num in range(33):
    print(f'range(33): {num}')
for num in range(0, 100, 5):
    print(f'range(100, setp 5): {num}')