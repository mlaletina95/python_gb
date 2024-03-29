"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.

Программа возвращает номер попытки с который была отгадана
загадка или ноль, если попытки исчерпаны
"""

def mystery(question: str, answers: list, chances: int) -> int:
    print(question)
    for i in range(chances):
        ans = input('Введите ответ:')
        if ans in answers:
            return i + 1
    return 0


if __name__ == '__main__':
    questions = {
        "Зимой и летом одним цветом": ['Елка', 'Ель', 'Елочка'],
        "Мягкие лапки, а в лапках царапки": ['Кот', 'Кошка', 'Котенок'],
        "По лесу осенью холодной он хмурый бродит и голодный": ['Волк', 'Волчонок'],
        "Где-то прячется в лесах очень хитрая": ['Лиса', 'Лисица'],
    }
    chances = 5
    for question, answers in questions.items():
        print(mystery(question, answers, chances))
