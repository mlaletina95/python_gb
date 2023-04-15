class Rect:
    def __init__(self, a: int, b: int):
        """Прямоугольник определен сторонами a и b"""
        self.a = a
        self.b = b

    def length(self):
        """Периметр прямоугольника"""
        return 2 * self.a + 2 * self.b

    def __add__(self, other):
        """Сложение прямоугольников"""
        return Rect(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        """Разность прямоугольников"""
        if self.length() > other.length():
            return Rect(self.a - other.a, self.b - other.b)
        else:
            return Rect(other.a - self.a, other.b - self.b)

    def __str__(self):
        return f"Прямоугольник {self.a} на {self.b}"

    def __repr__(self):
        return f"Rect({self.a}x{self.b})"


if __name__ == '__main__':
    r1 = Rect(100, 60)
    r2 = Rect(50, 30)
    print("Первый", r1)
    print("Второй", r2)

    print("Сумма", r1 + r2)
    print("Разность", r1 - r2)
    print("Разность", r2 - r1)

    help(Rect)