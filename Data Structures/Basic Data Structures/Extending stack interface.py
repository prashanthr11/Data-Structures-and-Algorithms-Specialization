import time as t

st = t.time()
l = []
ans = []

for i in range(int(input())):
    s = input().split()
    if len(s) == 2:
        x = int(s[1])
        if len(ans):
            ans.append(max(ans[-1], x))
        else:
            ans.append(x)
        l.append(x)
    else:
        if s == ['pop']:
            l.pop()
            ans.pop()
        else:
            print(ans[-1])

end = t.time()

# print(abs(end-st))
