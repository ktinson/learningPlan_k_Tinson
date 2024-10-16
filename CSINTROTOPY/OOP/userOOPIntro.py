class Person:
    def __init__(self, name, position, fitness):
        if not name:
            raise ValueError("Input missing")
        self.name = name
        self.position = position
        self.fitness = fitness
    def __str__(self):
        return f"I'm a person and my name is {self.name} and my position is {self.position}"
    @classmethod#makes more sense to create a class and use class methods
    def get(cls):
        name = input("Name: ")
        position = input("Position: ")
        fitness = input("Fitness level: ")
        return cls(name, position, fitness)
    #Getter
    @property
    def position(self):
        return self._position#the underscore allows for there not to be name clashes
    #Setter
    @position.setter
    def position(self, position):
        self._position = position
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
    # name = get_name()#created specific functions 
    # position = get_position()
    # person = get_person()
    # personD = get_perDict()#assigned these variable to a dictionary object in implementation

    personC = get_perClass()#used a class to define a person and create person objects
    personC.position = input("positon using setter overides the positon in perClass:")
    print(f'This is using a class: {personC.name} and they are {personC.position}')
    print(personC)#using __str__ to define object as a string using the PErson class
    print(personC.workout())#prompts user for fitness level using the Person Class workout method using the 
    finalPerson = Person.get()#using class methods is simpler making this faster
    print(finalPerson)
    print(finalPerson.workout())
    # print(f'{name} and {position}') #using the functions
    # print(f'{person[0]} and {person[1]}')#using person function
    # print(f"{personD['nameD']} and {personD['positionD']}")#using the Dict
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