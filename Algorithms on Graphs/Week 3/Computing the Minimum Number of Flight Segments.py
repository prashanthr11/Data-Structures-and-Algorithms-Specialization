from collections import defaultdict as dt


def solve(s, e):
    l = [[s]]
    cnt = 1
    
    while l:
        front = l.pop(0)
        
        tmp = list()
        
        for i in front:
            if not visited[i]:
                visited[i] = True
                for j in d[i]:
                    if not visited[j]:
                        tmp.append(j)
            
        if e in tmp:
            return cnt
            
        if len(tmp):
            l.append(tmp)
            
        cnt += 1
        
    return -1
    

n, m = map(int, input().split())
d = dt(list)

visited = [False] * (n + 1)
visited[0] = True

for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
    
s, e = map(int, input().split())

print(solve(s, e))
