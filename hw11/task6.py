class Matrix:
    def __init__(self, matrix):
        """Матрица"""
        self.matrix = matrix

    def __add__(self, other):
        new_matrix = []
        for row_index, row in enumerate(self.matrix):
            new_row = []
            for col_index, col in enumerate(row):
                new_row.append(col + other.matrix[row_index][col_index])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __sub__(self, other):
        new_matrix = []
        for row_index, row in enumerate(self.matrix):
            new_row = []
            for col_index, col in enumerate(row):
                new_row.append(col - other.matrix[row_index][col_index])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __str__(self):
        m = str(self.matrix)
        return m

    def __repr__(self):
        l1 = len(self.matrix)
        l2 = len(self.matrix[0])
        return f"Matrix({l1}x{l2})"


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[4, 3], [2, 1]])
    print(m1)
    print(m2)
    print(m1 + m2)
    print(m1 - m2)
