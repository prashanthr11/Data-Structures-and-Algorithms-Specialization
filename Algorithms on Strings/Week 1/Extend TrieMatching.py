def solve(s, pat):
    ln = len(pat)
    l = list()

    for i in range(len(s) - ln + 1):
        if s[i:i + ln] == pat:
            l.append(i)
    return l

from collections import  Counter as di

s = input()
ans = list()
for i in range(int(input())):
    x = solve(s, input())
    ans += x

d = di(ans)
ans = sorted(d.keys())
print(*ans)
