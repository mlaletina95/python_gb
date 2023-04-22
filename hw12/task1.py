import csv
class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Can not delete {self.param_name}')

    def validate(self, name):
        if name[0] < "A" or name[0] > "Z":
            raise TypeError(f"{self.param_name} should start with capitalized letter")
        for letter in name[1:]:
            if letter < "a" or letter > "z":
                raise TypeError(f"{self.param_name} should contain alphabet letters")


class Student:
    first_name = Name()
    last_name = Name()

    def __init__(self, first_name, last_name, file_name):
        self.first_name = first_name
        self.last_name = last_name
        self.scores = {}

        with open(file_name, "r") as f:
            reader = csv.DictReader(f, fieldnames=["item","score"])
            for line in reader:
                self.scores[line["item"]] = int(line["score"])
    def calc_average(self):
        scores = self.scores.values()
        return sum(scores) / len(scores)


    def info(self):
        print(self.first_name, self.last_name, self.calc_average())

if __name__ == '__main__':
    s = Student("Ivan", "Petrov", "Ivan.csv")
    s.info()