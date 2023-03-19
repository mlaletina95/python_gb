"""
Создайте функцию генератор чисел Фибоначчи
"""

def fib(n):
    a = 0
    b = 1
    
    for _ in range(n):
        yield a

        t = b
        b = a + b
        a = t

print(list(fib(10)))