import logging

logging.basicConfig(filename="./log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


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
            logging.error("Невозможно создать прямоугольник со стороной a=%s", a)
            raise RectSideAError("A must be > 0")
        self.a = a
        if b is not None:
            if b <= 0:
                logging.error("Невозможно создать прямоугольник со стороной b=%s", b)

                raise RectSideBError("B must be > 0")
            self.b = b
        else:
            self.b = a
        logging.debug("Создан прямоугольник со сторонами a=%s b=%s", self.a, self.b)

    def get_length(self):
        logging.debug("Вызвали метод вычисления периметра")
        return self.a + self.b + self.a + self.b

    def get_square(self):
        logging.debug("Вызвали метод вычисления площади")
        return self.a * self.b


if __name__ == "__main__":
    a = int(input("A = "))
    b = int(input("B = "))
    rect = Rect(a, b)
    print(rect.get_length(), rect.get_square())
