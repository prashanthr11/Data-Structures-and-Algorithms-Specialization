def evalu(a, op, b):
    return eval(str(a) + op + str(b))


def MinandMax(mini, maxi, i, j, op):
    minn, maxx = float('inf'), float('-inf')

    for x in range(i, j):
        a = evalu(mini[i][x], op[x], mini[x + 1][j])
        b = evalu(maxi[i][x], op[x], maxi[x + 1][j])
        c = evalu(mini[i][x], op[x], maxi[x + 1][j])
        d = evalu(maxi[i][x], op[x], mini[x + 1][j])

        minn = min(minn, a, b, c, d)
        maxx = max(maxx, a, b, c, d)

    return minn, maxx


def solve(digits, operators):
    ln = len(digits)
    mini = [[float('inf')] * ln for i in range(ln)]
    maxi = [[float('-inf')] * ln for i in range(ln)]

    row, col = 0, 0

    while row < ln and col < ln:
        mini[row][col] = maxi[row][col] = digits[row]
        row += 1
        col += 1

    for i in range(1, ln):
        x, y = 0, i
        while x < ln and y < ln:
            mini[x][y], maxi[x][y] = MinandMax(mini, maxi, x, y, operators)
            x += 1
            y += 1

    return maxi[0][-1]

s = input()
digits, operators = s[::2], s[1::2]
print(solve(digits, operators))