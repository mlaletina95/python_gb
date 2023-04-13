"""
Доработаем задачи 5. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from task5 import Animal, Dog, Fish, Bird


class AnimalFactory(Animal):
    def __new__(cls, animal_name, params):
        if animal_name == "dog":
            return Dog(**params)
        elif animal_name == "bird":
            return Bird(**params)
        elif animal_name == "fish":
            return Fish(**params)

if __name__ == "__main__":
    dog = AnimalFactory("dog", {"name": "Labrador", "fur_color": "brown"})
    bird = AnimalFactory("bird", {"name": "Owl", "feathers": True})
    fish = AnimalFactory("fish", {"name": "Salmon", "poisoned": False})
    dog.info()
    bird.info()
    fish.info()



