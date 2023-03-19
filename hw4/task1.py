"""
Напишите функцию для транспонирования матрицы
"""

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

"""
1  2  3
4  5  6
7  8  9
10 11 12

1 4 7 10
2 5 8 11
3 6 9 12
"""

def transpose(m):
    nm = []
    columns_len = len(m[0])
    rows_len = len(m)
    for i in range(columns_len):
        row = []
        for j in range(rows_len):
            row.append(m[j][i])
        nm.append(row)
    return nm

print("Matrix:")
for x in a:
    print(x)

print("Transposed Matrix:")
for x in transpose(a):
    print(x)
