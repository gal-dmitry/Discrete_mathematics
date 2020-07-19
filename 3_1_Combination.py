def output(combination):
    for i in range(len(combination) - 1):
        print(combination[i], end=' ')
    print(combination[-1])


def combo(step, k, n, i, top, top_global, combination):
    combination[step] = i
    if k == 0:
        output(combination)
        k += 1
        n += 1
        top -= 1
        step -= 1
    else:
        step += 1
        k -= 1
        n -= 1
        top += 1
        i += 1
        for j in range(i, min(top, top_global) + 1):
            combo(step, k, n, j, top, top_global, combination)


def main():
    k, n = (int(i) for i in input().split())
    if n == 0 or k == 0:
        return
    if k == 1:
        for i in range(n):
            print(i)
        return
    if k == n:
        for i in range(n):
            print(i, end=' ')
        return
    combination = [0 for i in range(k)]
    top_global = n - 1
    top = n - k
    j = 0
    k -= 1
    n -= 1
    step = 0
    for i in range(j, min(top, top_global) + 1):
        combo(step, k, n, i, top, top_global, combination)


if __name__ == "__main__":
    main()