def explore(i, lst, colour_lst):
    for j in lst[i]:
        if colour_lst[j] == 0:
            if colour_lst[i] == 1:
                colour_lst[j] = 2
            else:
                colour_lst[j] = 1
            explore(j, lst, colour_lst)


def checking(v, lst, colour_lst):
    for i in range(v):
        if lst[i]:
            for j in lst[i]:
                if colour_lst[i] == colour_lst[j]:
                    return 0
    return 1


def main():
    v, e = (int(i) for i in input().split())
    if e == 0:
        return print("YES")

    lst = [[] for i in range(v)]
    colour_lst = [0 for i in range(v)]

    for i in range(e):
        a, b = (int(i) for i in input().split())
        if a != b:
            lst[a - 1].append(b - 1)
            lst[b - 1].append(a - 1)
        else:
            return print("NO")

    for i in range(v):
        if colour_lst[i] == 0:
            colour_lst[i] = 1
            explore(i, lst, colour_lst)

    ind = checking(v, lst, colour_lst)
    if ind == 0:
        return print("NO")
    return print("YES")


if __name__ == "__main__":
    main()