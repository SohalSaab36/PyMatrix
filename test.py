from pymatrix import matrix

def main():
    # Create matrices
    A = matrix(2, 3, [3, 1, -1, 2, 3, 0])
    B = matrix(2, 3, [2, 5, 1, -2, 3, 0.5])
    C = matrix(3, 2, [1, 2, 3, 4, 5, 6])
    D = matrix(2, 2, [4, 7, 2, 6])
    I2 = matrix.identity(2)
    S = 2  # Scalar

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

    print("\nD * D.inverse() (Should be Identity):")
    print(D * D.inverse())

if __name__ == '__main__':
    main()
