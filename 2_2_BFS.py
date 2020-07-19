def main():
    v, e = (int(i) for i in input().split())
    lst = [[] for i in range(v)]
    distance = [v + 1 for i in range(v)]
    distance[0] = 0
    queue = [0]

    for i in range(e):
        a, b = (int(i) for i in input().split())
        lst[a].append(b)
        lst[b].append(a)

    while len(queue) > 0:
        c = int(queue.pop(0))
        for i in lst[c]:
            if distance[i] == v + 1:
                distance[i] = distance[c] + 1
                queue.append(i)

    for i in distance:
        print(i, end=' ')


if __name__ == "__main__":
    main()