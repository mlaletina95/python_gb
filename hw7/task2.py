import random

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def generate_name():
    s = ""
    n = random.randint(2, 4)
    for _ in range(n):
        s += random.choice(consonants) + random.choice(vowels)
    s = s.capitalize()
    return s

def write_random_names(filename):
    with open(filename, "a+") as f:
        f.write(generate_name())
        f.write("\n")


if __name__ == "__main__":
    write_random_names("names.txt")
