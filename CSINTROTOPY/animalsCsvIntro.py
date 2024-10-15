import csv

pets = []
with open("names.csv") as filename:
    reader = csv.reader(filename)
    for petType, environment in reader:
        pets.append({"petType": petType, "environment": environment })
with open("names.csv" ) as filename:
    for line in filename:
        row = line.rstrip().split(",")
        print(f'{row[0]} is in the{row[1]}')
with open("names.csv") as filename:
    for line in filename:
        petType, environment = line.rstrip().split(",")
        pet = {"petType": petType, "environment": environment }
        pets.append(pet)
for pet in sorted(pets, key=lambda pet: pet["petType"]):
    print(f'{pet['petType']} is in the{pet['environment']}')
        