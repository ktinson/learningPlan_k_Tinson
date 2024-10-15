def main():
    name = get_name()
    position = get_position()
    person = get_person()
    print(f'{name} and {position}') 
    print(f'{person[0]} and {person[1]}')

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