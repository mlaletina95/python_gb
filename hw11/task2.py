class Archive:
    _one = None
    def __init__(self, num: int, val: str):
        """Added num and val parameters"""
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        """Created new list for num and val, appends lists with numbers and values"""
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one.num)
            cls._one.values = [cls._one.val]
        return cls._one

    def __str__(self):
        return "Класс записывает число и строку в архив"

    def __repr__(self):
        return f"Archive({self.num}, {self.val})"


if __name__ == '__main__':
    s = Archive(1, "s1")
    s2 = Archive(2, "s2")
    s3 = Archive(3, "s3")

    print(s3.numbers, s3.values)
    print(s3.num, s3.val)
    print(s3)

    help(Archive)