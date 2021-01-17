def solve(n, l):
    ans = [[0 for i in range(n + 1)] for k in range(len(l) + 1)]
    
    for i in range(1, len(l) + 1):
        x = l[i - 1]
        for j in range(1, n + 1):
            if j < x:
                ans[i][j] = ans[i - 1][j]
            else:
                ans[i][j] = max(ans[i - 1][j], ans[i - 1][j - x] + x)
    
    return ans[-1][-1]


n, m = map(int, input().split())
l = list(map(int, input().split()))
print(solve(n, l))
