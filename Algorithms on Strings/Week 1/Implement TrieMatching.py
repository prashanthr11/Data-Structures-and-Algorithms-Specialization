def solve(s, pat):
    ln = len(pat)
    l = list()

    for i in range(len(s) - ln + 1):
        if s[i:i + ln] == pat:
            l.append(i)
    return l


s = input()
ans = list()
for i in range(int(input())):
    x = solve(s, input())
    ans += x

ans.sort()
print(*ans)
