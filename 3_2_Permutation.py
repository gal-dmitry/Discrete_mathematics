def output(permutation):
    for i in range(len(permutation) - 1):
        print(permutation[i], end=' ')
    print(permutation[-1])


def combo(i, step, permutation, n):
    permutation[step] = i
    if permutation[-1] != -1:
        output(permutation)
        step -= 1
    else:
        step += 1
        for j in range(n):
            if j not in permutation:
                combo(j, step, permutation, n)
        permutation[step] = -1


def main():
    n, k = (int(i) for i in input().split())
    if k == 1:
        for i in range(n):
            print(i)
    else:
        permutation = [-1 for i in range(k)]
        print(permutation)
        step = 0
        for i in range(n):
            if i not in permutation:
                combo(i, step, permutation, n)


if __name__ == "__main__":
    main()