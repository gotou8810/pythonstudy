from abc import ABC,abstractmethod

class Move(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Move):
    def move(self):
        print("歩く")

class Bird(Move):
    def move(self):
        print("飛ぶ")

human = Human()
human.move()

bird = Bird()
bird.move()
