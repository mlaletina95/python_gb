"""
Напишите следующие функции:
1. Нахождение корней квадратного уравнения
2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с
каждой тройкой чисел из csv файла.
4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import math
import csv
import random


def square_equation(a: float, b: float, c: float):
    # ax^2 + bx + c = 0
    d = b * b - 4 * a * c
    if d < 0:
        return None
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return [x1, x2]


def generate_numbers_csv():
    count = random.randint(100, 1000)
    with open("numbers.csv", "w+") as f:
        writer = csv.writer(f)
        for i in range(count):
            writer.writerow([
                random.randint(-100, 100),
                random.randint(-100, 100),
                random.randint(-100, 100)
            ])


if __name__ == "__main__":
    print(square_equation(3, 5, 2))
    generate_numbers_csv()