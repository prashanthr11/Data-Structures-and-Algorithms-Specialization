from collections import defaultdict as dt


def canreach(d, x, y, visited):
    if not d[x]:
        return False
    if y in d[x]:
        return True

    for i in d[x]:
        if i not in visited:
            if canreach(d, i, y, visited + [i]):
                return True

    return False


def solve():
    n, m = map(int, input().split())
    d = dt(list)
    for i in range(1, n + 1):
        d[i] = list()

    for i in range(m):
        u, v = map(int, input().split())
        d[u].append(v)
        d[v].append(u)

    x, y = map(int, input().split())
    return canreach(d, x, y, [])


print(1) if solve() else print(0)
