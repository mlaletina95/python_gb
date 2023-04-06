import random

def write_random_number(count: int, name: str):
    with open(name, "w") as file:
        for _ in range(count):
            ni = random.randint(-1000, 1000)
            nf = random.uniform(-1000, 1000)
            s = str(ni) + "|" + str(nf)
            file.write(s)
            file.write('\n')

write_random_number(10, 'numbers.txt')

