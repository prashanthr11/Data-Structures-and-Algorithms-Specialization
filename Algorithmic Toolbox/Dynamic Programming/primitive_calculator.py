def solve(n):
    if n == 1:
        return 0, [1]
    if n == 2:
        return 1, [1, 2]
    if n == 3:
        return 1, [1, 3]
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = dp[3] = 2

    for i in range(4, n + 1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3], dp[i - 1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1

    l = list()
    i = n

    while i > 1:
        l.append(i)
        tmp = dp[i]
        if i % 3 == 0 and i % 2 == 0:
            if dp[i // 3] + 1 == tmp:
                i //= 3
            elif dp[i // 2] + 1 == tmp:
                i //= 2
            else:
                i -= 1
        elif i % 3 == 0:
            if dp[i // 3] + 1 == tmp:
                i //= 3
            else:
                i -= 1
        elif i % 2 == 0:
            if dp[i // 2] + 1 == tmp:
                i //= 2
            else:
                i -= 1
        else:
            i -= 1
    l += [1]
    l.reverse()

    return dp[-1] - 1, l


n = int(input())
cnt, l = solve(n)
print(cnt)
print(*l)