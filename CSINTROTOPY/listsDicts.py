pets = ["dog", "cat", "shark", "unicorn", "cactus"] #list
enviroments = ["water", "forest", "town", "desert", "wherever"]
theyLive = zip(pets, enviroments)
print(set(theyLive))
for pet in pets:
    print(f'{pet}\n', end ="")
    print("Pet: " + pet)
for i in range(len(pets)):
    print(i + 1, pets[i])
shoes = {
    "flipflops": "Beach",
    "boots": "Mountains",
    "sneakers": "streets",
    "slippers": "house",
}#dict
print(f'where do you wear flipflops: {shoes["flipflops"]}')
for shoe in shoes:
    print(shoe, shoes[shoe], sep=", ")
