class salary(str):
    def __lt__(a, b):
        return a + b > b + a


def solve(l):
    l = list(map(str, l))
    ret = sorted(l, key=salary)
    ret = ''.join(ret)
    return ret if int(ret) else '0'


n = int(input())
l = list(map(int, input().split()))
print(solve(l))