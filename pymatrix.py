import math

class matrix:
    def __init__(self, row, column, customvals=[]):
        self.row = row
        self.column = column
        self.order = str(row) + 'x' + str(column)
        self.amt = row * column
        self.elements = customvals
        self.values = []

        if len(customvals) == 0:
            for i in range(row):
                self.values.append([])
                for j in range(column):
                    self.values[i].append('a' + str(i+1) + str(j+1))
        else:
            if len(customvals) != self.amt:
                raise ValueError("Custom values do not match matrix size")
            index = 0
            for i in range(row):
                self.values.append([])
                for j in range(column):
                    self.values[i].append(customvals[index])
                    index += 1

    def transpose(self):
        transposed_elements = []
        for j in range(self.column):
            for i in range(self.row):
                transposed_elements.append(self.values[i][j])
        return matrix(self.column, self.row, transposed_elements)

    def __add__(self, other):
        if self.order != other.order:
            raise ValueError("Matrix dimensions must match for addition")
        return matrix(self.row, self.column, [
            self.values[i][j] + other.values[i][j]
            for i in range(self.row) for j in range(self.column)
        ])

    def __sub__(self, other):
        if self.order != other.order:
            raise ValueError("Matrix dimensions must match for subtraction")
        return matrix(self.row, self.column, [
            self.values[i][j] - other.values[i][j]
            for i in range(self.row) for j in range(self.column)
        ])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return matrix(self.row, self.column, [
                self.values[i][j] * other
                for i in range(self.row) for j in range(self.column)
            ])
        elif isinstance(other, matrix):
            if self.column != other.row:
                raise ValueError("Matrix dimensions must be compatible for multiplication")
            result_elements = []
            for i in range(self.row):
                for j in range(other.column):
                    value = sum(self.values[i][k] * other.values[k][j] for k in range(self.column))
                    result_elements.append(value)
            return matrix(self.row, other.column, result_elements)
        else:
            raise ValueError("Operand must be a scalar or a matrix")

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        return self.values == other.values

    def __pow__(self, power):
        if self.row != self.column:
            raise ValueError("Only square matrices can be raised to a power")
        if power == 0:
            return matrix.identity(self.row)
        result = self
        for _ in range(1, power):
            result = result * self
        return result

    def determinant(self):
        if self.row != self.column:
            raise ValueError("Determinant can only be computed for square matrices")
        if self.row == 1:
            return self.values[0][0]
        if self.row == 2:
            return self.values[0][0]*self.values[1][1] - self.values[0][1]*self.values[1][0]
        det = 0
        for c in range(self.column):
            minor = matrix(self.row - 1, self.column - 1, [
                self.values[i][j]
                for i in range(1, self.row)
                for j in range(self.column) if j != c
            ])
            det += ((-1) ** c) * self.values[0][c] * minor.determinant()
        return det

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")

        if self.row == 2:
            a, b = self.values[0]
            c, d = self.values[1]
            inv_vals = [d, -b, -c, a]
            return matrix(2, 2, [x / det for x in inv_vals])

        cofactors = []
        for r in range(self.row):
            cofactor_row = []
            for c in range(self.column):
                minor = matrix(self.row - 1, self.column - 1, [
                    self.values[i][j]
                    for i in range(self.row) if i != r
                    for j in range(self.column) if j != c
                ])
                cofactor = ((-1) ** (r + c)) * minor.determinant()
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
        cof_matrix = matrix(self.row, self.column, [elem for row in cofactors for elem in row])
        adjugate = cof_matrix.transpose()
        return (1 / det) * adjugate

    @staticmethod
    def identity(n):
        return matrix(n, n, [1 if i == j else 0 for i in range(n) for j in range(n)])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.values])
#################################################################################################################
# Test program
    
def main():
    # Create matrices
    A = matrix(2, 3, [3, 1, -1, 2, 3, 0])
    B = matrix(2, 3, [2, 5, 1, -2, 3, 0.5])
    C = matrix(3, 2, [1, 2, 3, 4, 5, 6])
    D = matrix(2, 2, [4, 7, 2, 6])
    I2 = matrix.identity(2)
    S = 2  # scalar

    print("Matrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nMatrix C (for multiplication):")
    print(C)

    print("\nMatrix D (square matrix):")
    print(D)

    print("\nIdentity Matrix (2x2):")
    print(I2)

    print("\nA + B:")
    print(A + B)

    print("\nA - B:")
    print(A - B)

    print("\nTranspose of A:")
    print(A.transpose())

    print("\nA * scalar (2):")
    print(A * S)

    print("\nA * C:")
    print(A * C)

    print("\nD == D:")
    print(D == D)

    print("\nD ** 2:")
    print(D ** 2)

    print("\nDeterminant of D:")
    print(D.determinant())

    print("\nInverse of D:")
    print(D.inverse())

    print("\nD * D.inverse():")
    print(D * D.inverse())  # Should be close to identity

    input() 
if __name__ == '__main__':
    main()