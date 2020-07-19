def explore(i, lst, visited):
    for j in lst[i]:
        if visited[j] == 0:
            visited[j] = 1
            explore(j, lst, visited)


def main():
    v, e = (int(i) for i in input().split())
    lst = [[] for i in range(v)]
    visited = [0 for i in range(v)]
    count = 0

    for i in range(e):
        a, b = (int(i) for i in input().split())
        lst[a - 1].append(b - 1)
        lst[b - 1].append(a - 1)

    for i in range(v):
        if visited[i] == 0:
            visited[i] = 1
            count += 1
            explore(i, lst, visited)

    print(count)


if __name__ == "__main__":
    main()