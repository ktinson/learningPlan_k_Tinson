x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))
print(f'Boolean X{x} is greater than y{y}: {x > y}')
if x > y:
    print(f'x = {x} is greater than y = {y}')
elif x < y:
    print(f'x = {x} is less than y = {y}')
else:
    print(f'x = {x} is equals y = {y}')