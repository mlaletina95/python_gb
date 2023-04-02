"""
Создайте модуль и напишите в нём функцию, которая получает на вход
дату в формате DD.MM.YYYY Функция возвращает истину, если дата может
существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def check_date(date):
    day, month, year = date.split(".")
    day = int(day)
    month = int(month)
    year = int(year)

    if year < 1 or year > 9999:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    # апрель, июнь, сентябрь, ноябрь имеют 30 дней
    if month in [4, 6, 9, 11] and day > 30:
        return False
    # февраль
    elif month == 2:
        if _check_leap_year(year) and day > 29:
            return False
        elif not _check_leap_year(year) and day > 28:
            return False
    elif day > 31:
        return False

    return True


def _check_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    date = input("Введите дату: ")
    if check_date(date):
        print("Дата существует")
    else:
        print("Дата не существует")
