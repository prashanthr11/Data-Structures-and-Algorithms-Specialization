'''
Time Complexity: O((V + E) * Log N)
Space Complexity: O(V)
'''

from heapq import *
from collections import defaultdict


def solve(source, cost, visited, d):
    pq = [(0, source)]

    while pq:   # O(V)
        wt, source = heappop(pq)
        '''
        As heaps in python doesn't support modifing priorities. So, we
        have to store all the modified distances for each vertex. In the
        worst case, we store all modified distances and vertices. Although,
        we are processing each vertex once. but the storing is costly.
        So, The Time complexity of min heap is O(Log N). Where N is the
        size of the min heap.
        '''
        if not visited[source]:
            visited[source] = True
            for y, w in d[source]:      # O(E)
                if cost[y] > cost[source] + w:
                    cost[y] = cost[source] + w
                    heappush(pq, (cost[y], y))      # O(Log N)


def main():
    n, m = map(int, input().split())
    d = defaultdict(list)
    cost = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    for i in range(m):
        a, b, w = map(int, input().split())
        d[a].append((b, w))

    source, destination = map(int, input().split())
    cost[source] = 0

    solve(source, cost, visited, d)

    # print(*cost)
    return cost[destination] if cost[destination] != float('inf') else -1


if __name__ == '__main__':
    print(main())
