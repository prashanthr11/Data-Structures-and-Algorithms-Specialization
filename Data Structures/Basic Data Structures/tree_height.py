import sys
import threading
from collections import defaultdict as dt

ret = 0


class Trie:
    def __init__(self,val=0):
        self.val = val
        self.childrens = list()


def getHeight(root, heads, cnt):
    if not heads[root].childrens:
        global ret
        ret = max(cnt + 1, ret)
        return

    for i in heads[root].childrens:
        # print(f'root is {root} and child is {i}: {cnt}')
        getHeight(i, heads, cnt + 1)


def solve(l):
    heads = list()
    root = None

    for i in l:
        heads.append(Trie(i))

    for i, a in enumerate(l):
        if a == -1:
            root = i
        else:
            heads[a].childrens.append(i)

    getHeight(root, heads, 0)


def main():
    n = int(input())
    l = list(map(int, input().split()))
    solve(l)
    print(ret)


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
