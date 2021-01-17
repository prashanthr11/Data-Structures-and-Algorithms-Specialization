n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pos = [i for i in b if i >= 0]
neg = [i for i in b if i < 0]

pos.sort()
neg.sort()
a.sort()

res = 0

for i in a:
    if i >= 0:
        if len(pos):
            res += i * min(pos)
            pos.remove(min(pos))
        else:
            res += i * max(neg)
            neg.remove(max(neg))
    else:
        if len(neg):
            res += i * min(neg)
            neg.remove(min(neg))
        else:
            res += i * min(pos)
            pos.remove(min(pos))
print(res)
