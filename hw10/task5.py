class Animal():
    def __init__(self, name):
        self.name = name

    def info(self):
        print(self.name)


class Dog(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def info(self):
        print(self.name, "fur color", self.fur_color)


class Fish(Animal):
    def __init__(self, name, poisoned):
        super().__init__(name)
        self.poisoned = poisoned

    def info(self):
        print(self.name, "poisoned", self.poisoned)

class Bird(Animal):
    def __init__(self, name, feathers):
        super().__init__(name)
        self.feathers = feathers

    def info(self):
        print(self.name, "feathers", self.feathers)

if __name__ == "__main__":
    dog = Dog("Labrador", "brown")
    bird = Bird("Owl", True)
    fish = Fish("Salmon", False)

    dog.info()
    bird.info()
    fish.info()

