from collections import defaultdict as dt


def solve(s):
    visited[s] = True
    
    for i in d[s]:
        if not visited[i]:
            solve(i)
            ans.append(i)
            
    return



n, m = map(int, input().split())
d = dt(list)

for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    

visited = [False] * (n + 1)
visited[0] = True
ans = list()

for i in range(1, n + 1):
    if not visited[i]:
        solve(i)
        ans.append(i)

ans.reverse()
print(*ans)