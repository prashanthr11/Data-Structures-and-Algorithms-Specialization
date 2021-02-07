from collections import defaultdict as dt, deque as dq

def hashh(s):
    ret = 0
    MOD = 10**9+7
    for i, a in enumerate(s):
        ret += (263 ** i) * ord(a)
        
    return (ret % MOD) % m


def add(idx, tmp):
    if tmp not in d[idx]:
        d[idx].appendleft(tmp)
        


def check(b):
    for i in d[b]:
        print(i, end=' ')
    print()
    
m = int(input())
d = dt(dq)
for i in range(int(input())):
    a, b = input().split()
    if a == 'add':
        tmp = hashh(b)
        add(tmp, b)
    elif a == 'check':
        check(int(b))
    elif a == 'find':
        tmp = hashh(b)
        print('yes') if b in d[tmp] else print('no')
    else:
        tmp = hashh(b)
        if b in d[tmp]:
            d[tmp].remove(b)