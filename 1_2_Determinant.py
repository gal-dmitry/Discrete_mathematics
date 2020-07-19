def first_row_column(matrix, n, k):
    n -= 1
    k *= matrix[0][0]
    matrix.remove(matrix[0])
    for i in range(n):
        matrix[i].remove(matrix[i][0])
    return matrix, n, k


def division(matrix, n, k):
    for i in range(1, n):
        c = matrix[i][0] / matrix[0][0]
        for j in range(n):
            matrix[i][j] -= c * matrix[0][j]
    return first_row_column(matrix, n, k)


def swap(matrix, n, k):
    for i in range(1, n):
        if matrix[i][0] != 0:
            matrix[0], matrix[i] = matrix[i], matrix[0]
            k *= -1
            break
    return matrix, k


def gauss(matrix, n, k):
    if n == 1:
        return print(round(k * matrix[0][0]))
    if matrix[0][0] == 0:
        matrix, k = swap(matrix, n, k)
        if matrix[0][0] == 0:
            return print(0)
    matrix, n, k = division(matrix, n, k)
    return gauss(matrix, n, k)


def main():
    n = int(input())
    k = 1
    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = input().split()
        for j in range(n):
            matrix[i][j] = int(matrix[i][j])
    return gauss(matrix, n, k)


if __name__ == "__main__":
    main()