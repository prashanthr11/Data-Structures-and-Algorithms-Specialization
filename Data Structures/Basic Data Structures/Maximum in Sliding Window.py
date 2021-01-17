from collections import deque as dq

def solve(l, k, n):

    maxi = dq()
    ret = list()

    for i in range(k):
        while len(maxi) > 0 and l[maxi[-1]] < l[i]:
            maxi.pop()

        maxi.append(i)
    ret.append(l[maxi[0]])

    for i in range(k, n):
        while len(maxi) > 0 and maxi[0] <= i - k:
            maxi.popleft()

        while len(maxi) > 0 and l[maxi[-1]] < l[i]:
            maxi.pop()

        maxi.append(i)
        ret.append(l[maxi[0]])

    return ret

n = int(input())
l = list(map(int, input().split()))
k = int(input())
print(*solve(l, k, n))