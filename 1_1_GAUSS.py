def output(matrix, n):
    print('YES')
    for i in range(n):
        print(matrix[i][n], end=' ')


def derivatives(matrix, n):
    for i in range(n):
        matrix[i][n] /= matrix[i][i]
        matrix[i][i] = 1
    return output(matrix, n)


def solving(matrix, n, m):
    null_string = [0] * (m + 1)
    while null_string in matrix:
        matrix.remove(null_string)
        n -= 1
    for i in range(n):
        if (matrix[i][m] != 0) and (matrix[i][:-1] == [0] * m):
            return print('NO')
    if m > n:
        return print("INF")
    return derivatives(matrix, n)


def gauss_bottom_up(matrix, n, m, border):
    for i in reversed(range(border)):
        if matrix[i][i] == 0:
            continue
        for j in reversed(range(i)):
            c = matrix[j][i] / matrix[i][i]
            if c != 0:
                for t in range(i, m + 1):
                    matrix[j][t] -= c * matrix[i][t]
    return solving(matrix, n, m)


def gauss_top_down(matrix, n, m, border):
    for i in range(border):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            if matrix[i][i] == 0:
                continue
        for j in range(i + 1, n):
            c = matrix[j][i] / matrix[i][i]
            if c != 0:
                for t in range(i, m + 1):
                    matrix[j][t] -= c * matrix[i][t]
    return gauss_bottom_up(matrix, n, m, border)


def main():
    n, m = (int(i) for i in input().split())
    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = input().split()
        for j in range(m + 1):
            matrix[i][j] = int(matrix[i][j])
    border = min(n, m)
    return gauss_top_down(matrix, n, m, border)


if __name__ == "__main__":
    main()