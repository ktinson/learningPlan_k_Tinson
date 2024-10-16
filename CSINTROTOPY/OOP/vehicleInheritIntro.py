class Vehicle:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...
class Car(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels
    ...   
class Plane(Vehicle):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings
    ...
car = Car("volvo", "4")
plane = Plane("airplane", "2")
print(f'There is a  {car.name} with {car.wheels} wheels and a {plane.name} with {plane.wings} wings')