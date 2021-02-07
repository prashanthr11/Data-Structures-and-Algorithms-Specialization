from math import log2, floor as fl

def getparent(i):
    return  i // 2 if i % 2 else (i // 2) - 1


def getchild(n):
    return (2 * n + 1, 2 * n + 2)

def solve(n, l):
    if n <= 0:
        return
    tmp = getparent(n)
    if l[tmp] > l[n]:
        l[tmp], l[n] = l[n], l[tmp]
        ret.append((tmp, n))
    solve(tmp, l)
    lft, rt = getchild(n)
        
    if lft < len(l) and l[lft] < l[n]:
        l[lft], l[n] = l[n], l[lft]
        ret.append((lft, n))
        solve(lft, l)
    if rt < len(l) and l[rt] < l[n]:
        l[rt], l[n] = l[n], l[rt]
        ret.append((rt, n))
        solve(rt, l)

ret = list()
n = int(input())
l = list(map(int, input().split()))

for i in range(n - 1, - 1, -1):
    solve(i, l)
    
print(len(ret))
for x, y in ret:
    print(x, y)