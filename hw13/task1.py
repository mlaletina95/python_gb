

class RectError(Exception):
    pass

class RectSideError(RectError):
    pass

class RectSideAError(RectSideError):
    pass


class RectSideBError(RectSideError):
    pass

class Rect:
    def __init__(self, a: float, b: float = None):
        if a <= 0:
            raise RectSideAError("A must be > 0")
        self.a = a
        if b is not None:
            if b <= 0:
                raise RectSideBError("B must be > 0")
            self.b = b
        else:
            self.b = a

    def get_length(self):
        return self.a + self.b + self.a + self.b

    def get_square(self):
        return self.a * self.b


if __name__ == "__main__":
    rect = Rect(10, 20)
    print(rect.get_length(), rect.get_square())

    rect2 = Rect(10)
    print(rect2.get_length(), rect2.get_square())

    try:
        rect3 = Rect(20, -30)
        print(rect3.get_length(), rect3.get_square())
    except RectSideAError:
        print("Ошибка стороны А прямоугольника")
    except RectSideBError:
        print("Ошибка стороны B прямоугольника")
