from collections import defaultdict as dt
from collections import deque


def isbipartite(queue, white, black, visited, d):
	while queue:
		# print(*queue)
		# print(white)
		# print(black)
		front, iswhite = queue.popleft()
		visited[front] = True


		for i in d[front]:
			if not visited[i]:
				if iswhite:
					if i in white:
						return 0
					else:
						black.add(i)
				else:
					if i in black:
						return 0
					else:
						white.add(i)

				queue.append((i, not iswhite))

	return 1


def main():
	n, m = map(int, input().split())
	d = dt(list)

	for i in range(m):
		x, y = map(int, input().split())
		d[x].append(y)
		d[y].append(x)


	visited = [False] * (n + 1)
	visited[0] = True
	white, black = set(), set()
	white.add(1)


	for i in range(1, n + 1):
		if not visited[i]:
			if not isbipartite(deque([(i, True)]), white, black, visited, d):
				return 0

	return 1
	

if __name__ == '__main__':
	print(main())