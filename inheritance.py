from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def fuel(self):
        pass

class Car(Vehicle):
    def fuel(self):
        print("gasoline")

car = Car("honda")
car.fuel()