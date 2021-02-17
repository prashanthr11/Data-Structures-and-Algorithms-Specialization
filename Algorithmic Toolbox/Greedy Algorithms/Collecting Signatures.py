def solve(l):
    l.sort()
    first, second = l[0][0], l[0][1]
    ret = list()
    
    for i in range(1, len(l)):
        if second < l[i][0]:
            ret.append(second)
            second = l[i][1]
        else:
            second = min(second, l[i][1])
            
    ret.append(second)
    return ret


l = list()

for i in range(int(input())):
    l.append(tuple(map(int, input().split())))
    
    
ret = solve(l)
print(len(ret))
print(*ret)