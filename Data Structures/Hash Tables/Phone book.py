d = dict()
for i in range(int(input())):
    l = input().split()
    
    if l[0] == 'add':
        d[l[1]] = l[2]
    if l[0] == 'find':
        if l[1] in d:
            print(d[l[1]])
        else:
            print('not found')
    if l[0] == 'del':
        if l[1] in d:
            del d[l[1]]