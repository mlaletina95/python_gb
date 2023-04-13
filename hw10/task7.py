from hw6 import mystery


class Mystery:
    def __init__(self, questions, chances):
        self.questions = questions
        self.chances = chances

    def ask(self):
        for question, answers in self.questions.items():
            print(mystery(question, answers, self.chances))


if __name__ == '__main__':
    questions = {
        "Зимой и летом одним цветом": ['Елка', 'Ель', 'Елочка'],
        "Мягкие лапки, а в лапках царапки": ['Кот', 'Кошка', 'Котенок'],
        "По лесу осенью холодной он хмурый бродит и голодный": ['Волк', 'Волчонок'],
        "Где-то прячется в лесах очень хитрая": ['Лиса', 'Лисица'],
    }
    chances = 5
    m = Mystery(questions, chances)
    m.ask()


