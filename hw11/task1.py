import time

class MyString(str):
    def __new__(cls, value: str, author: str):
        """Моя строка содержит значение, автора и время"""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __repr__(self):
        return f"MyString({self, self.author, self.time})"

if __name__ == '__main__':

    s = MyString("stroka", author="Marina")
    print(s, s.author, s.time)

    help(MyString)