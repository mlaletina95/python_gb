# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
a = [1, 2, 3, 1, 2, 3, 5, 6, 1]

na = []

for x in a:
    if x not in na:
        na.append(x)

print(na)
