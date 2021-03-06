

class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = [[0]]
        self.matrix = matrix

    def input(self):
        self.matrix = []
        line = int(input("Введите количество строк матрицы - "))
        column = int(input("Введите количество столбцов матрицы - "))
        for _ in range(line):
            tn = []
            for _ in range(column):
                k = int(input("ведите число - \t"))
                tn.append(k)
            self.matrix.append(tn)

    def __str__(self):
        return "\n".join(["\t".join(map(str, x)) for x in self.matrix])


class DetOfMatrix2x2(Matrix):
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0, 0], [0, 0]]
        super().__init__(spisok)
        if not self._is_valid():
            raise ValueError("Ваша матрица должна быть 2x2")

    def input(self):
        super().input()
        if not self._is_valid():
            raise ValueError("Ваша матрица должна быть 2x2")

    def _is_valid(self) -> bool:
        if len(self.matrix) != 2:
            return False
        elif len(self.matrix[0]) != 2:
            return False
        elif len(self.matrix[1]) != 2:
            return False
        return True

    def determinant(self):
        pos_one = self.matrix[0][0] * self.matrix[1][1]
        pos_two = self.matrix[0][1] * self.matrix[1][0]
        return pos_one - pos_two


m = DetOfMatrix2x2()
m.input()
print("Ваша матрица:\n")
print(m)
print("\nОпределитель матрицы равен " + str(m.determinant()))
