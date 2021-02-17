def solve(n, m):
    n, m = n % 60, m % 60
        
    pre, arr = list(), list()
    
    arr.append(0)
    pre.append(0)
    
    arr.append(1)
    pre.append(1)
    
    for i in range(2, 61):
        arr.append((arr[i - 1] + arr[i - 2]) % 10)
        pre.append(pre[i - 1] + arr[i])

    if n > m:
        tmp = (pre[-1] - pre[n - 1]) % 10
        tmp += pre[m]
        return tmp % 10
    else:
        return (pre[m] - pre[n - 1]) % 10

    

n, m = map(int, input().split())
print(solve(n % 60, m % 60))
