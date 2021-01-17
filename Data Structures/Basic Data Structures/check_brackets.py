def solve(s):
    l = list()

    for i, a in enumerate(s):
        if a in '({[':
            l.append((i, a))
        elif a in ')}]':
            if not len(l):
                return i + 1
            else:
                if a == ')':
                    if l[-1][1] == '(':
                        l.pop()
                    else:
                        return i + 1

                if a == ']':
                    if l[-1][1] == '[':
                        l.pop()
                    else:
                        return i + 1
                if a == '}':
                    if l[-1][1] == '{':
                        l.pop()
                    else:
                        return i + 1

    if len(l):
        return l[0][0] + 1

    return 'Success'


s = input()
print(solve(s))