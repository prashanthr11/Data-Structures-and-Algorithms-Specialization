from collections import defaultdict as dt
import sys



def main():
	sys.setrecursionlimit(200000)
	n, m = map(int, input().split())
	d = dt(list)

	for i in range(m):
		x, y = map(int, input().split())
		d[x].append(y)
		d[y].append(x)

	source, destination = map(int, input().split())
	queue = [(source, 0)]
	visited = [False] * (n + 1)
	visited[0] = True
	visited[source] = True

	while queue:
		# print(*queue)
		front, cnt = queue.pop(0)
		if front == destination:
			return cnt

		for i in d[front]:
			if not visited[i]:
				visited[i] = True
				queue.append((i, cnt + 1))

	return -1
	

if __name__ == '__main__':
	print(main())
