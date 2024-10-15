class Person:
    def __init__(self, name, position, fitness):
        if not name:
            raise ValueError("Input missing")
        self.name = name
        self.position = position
        self.fitness = fitness
    def __str__(self):
        return f"I'm a person and my name is {self.name} and my position is {self.position}"
    def workout(self):
        match self.fitness:
            case "Lazy":
                return "😴"
            case "Sedenatary":
                return "🗻"
            case "Moderate":
                return "🤸🏿‍♂️"
            case "Extreme":
                return "🐎"
            case _:
                return "🌪️"

def main():
    name = get_name()
    position = get_position()
    person = get_person()
    personD = get_perDict()
    personC = get_perClass()
    print(f'This is using a class: {personC.name} and they are {personC.position}')
    print(personC)
    print(personC.workout())
    print(f'{name} and {position}') 
    print(f'{person[0]} and {person[1]}')
    print(f"{personD['nameD']} and {personD['positionD']}")
def get_perClass():
    name = input("Name:")
    position = input("Position: ")
    fitness = input("Fitness level: ")
    try:
        return Person(name, position, fitness)
    except ValueError:
        get_perClass()

def get_perDict():
    nameD = input("Name: ")
    positionD = input("Position: ")
    return{"nameD": nameD, "positionD": positionD}
def get_person():
    nameP = input("Name: ")
    positionP = input("Position: ")
    return [nameP, positionP]
def get_name():
    return input("Name: ")
def get_position():
    return input("Position: ")
if __name__=="__main__":
    main()