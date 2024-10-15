import csv

pets = []
with open("names.csv") as filename:
    reader = csv.reader(filename)
    readerDict = csv.DictReader(filename)
    for petType, environment, food in reader:
        pets.append({"petType": petType, "environment": environment, "food": food })
    for row in readerDict:
        pets.append({"petType": row["petType"], "environment": row["environment"], "food": row["food"] })
with open("names.csv" ) as filename:
    for line in filename:
        row = line.rstrip().split(",")
        print(f'{row[0]} is in the{row[1]}')
with open("names.csv") as filename:
    for line in filename:
        petType, environment, food = line.rstrip().split(",")
        pet = {"petType": petType, "environment": environment, "food": food }
        pets.append(pet)
for pet in sorted(pets, key=lambda pet: pet["petType"]):
    print(f'{pet['petType']} is in the{pet['environment']}')
    print(f'{pet['petType']} is in the {pet['environment']} and eats{pet['food']}')
        