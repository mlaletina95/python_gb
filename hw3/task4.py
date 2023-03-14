# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

items = {
    "book": 200,
    "water": 500,
    "laptop": 1200,
    "food": 1000,
    "clothes": 1500,
    "shoes": 800,
    "umbrella": 300,
}

capacity_grams = int(input("Bag capacity = "))
bag = []
for item, weight in items.items():
    if weight <= capacity_grams:
        bag.append(item)
        capacity_grams = capacity_grams - weight

print("Items in bag: ")
for item in bag:
    print(item)