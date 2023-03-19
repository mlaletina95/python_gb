"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ["John", "Ivan", "Diana"]
rates = [1000.0, 2000.0, 1500.0]
rewards = ["10.5%", "20%", "10%"]


def get_reward(rate, reward):
    reward_float = float(reward[:-1])
    return rate * reward_float / 100


print({name: get_reward(rate, reward)
       for name, rate, reward in zip(names, rates, rewards)})
