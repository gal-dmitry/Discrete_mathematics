def output(path, loop):
    for i in path:
        while loop[i] > 0:
            print(i + 1, end=' ')
            loop[i] -= 1
        print(i + 1, end=' ')


def loop_inserting(path):
    while len(path) > 1:
        for i in path:
            for j in path:
                if i != j and j[0] in i:
                    place = i.index(j[0]) + 1
                    for k in j[1:]:
                        i.insert(place, k)
                        place += 1
                    i.insert(place, j[0])
                    path.remove(j)
    return path[0]


def null_list(path):
    while [] in path:
        path.remove([])
    return path


def explore(x, lst, degree, path):
    degree[x] -= 2
    path.append(x)
    i = 0
    while i < len(lst[x]):
        if degree[lst[x][i]] == 0:
            i += 1
        else:
            break
    if i < len(lst[x]):
        a = lst[x][i]
        lst[x].remove(a)
        lst[a].remove(x)
        explore(a, lst, degree, path)


def bypass(v, lst, degree, path):
    for i in range(v):
        while degree[i] > 0:
            explore(i, lst, degree, path[i])
    return path, degree, lst


def parity(v, degree):
    for i in range(v):
        if degree[i] % 2 == 1 or degree[i] == 0:
            return 0
    return 1


def main():
    v, e = (int(i) for i in input().split())
    if v > e:
        return print('NONE')

    lst = [[] for i in range(v)]
    degree = [0 for i in range(v)]
    loop = [0 for i in range(v)]
    path = [[] for i in range(v)]

    for i in range(e):                                  # добавление ребер
        a, b = (int(i) for i in input().split())
        if a != b:
            lst[a - 1].append(b - 1)
            lst[b - 1].append(a - 1)
            degree[a - 1] += 1
            degree[b - 1] += 1
        else:
            loop[a - 1] += 1

    if not parity(v, degree):                           # проверка степеней вершин
        return print('NONE')

    path, degree, lst = bypass(v, lst, degree, path)    # пока все вершины не пройдены
    path = null_list(path)                              # выкидываем пустые циклы
    path = loop_inserting(path)                         # склейка петель
    return output(path, loop)                           # печать цикла


if __name__ == "__main__":
    main()
