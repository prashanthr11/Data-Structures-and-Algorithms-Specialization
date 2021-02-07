import heapq

n, m = map(int, input().split())
l = list(map(int, input().split()))

times = [(-0, i) for i in range(n)]
heapq.heapify(times)

i = 0
while i < m:
    ti, pr = heapq.heappop(times)
    print(pr, ti)
    heapq.heappush(times, (ti + l[i], pr))
    i += 1