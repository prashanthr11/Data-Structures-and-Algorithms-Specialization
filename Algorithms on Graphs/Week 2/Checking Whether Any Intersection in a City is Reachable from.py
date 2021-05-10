from collections import defaultdict as dt
import sys



def dfs(d, s, visited, lst):
	visited[s] = True

	for i in d[s]:
		if not visited[i]:
			dfs(d, i, visited, lst)

	lst.append(s)


def dfs_reverse(d, s, visited):
	visited[s] = True

	for i in d[s]:
		if not visited[i]:
			dfs_reverse(d, i, visited)
			


def main():
	sys.setrecursionlimit(200000)
	n, m = map(int, input().split())
	d = dt(list)
	d_transpose = dt(list)
	visited = [False] * (n + 1)
	visited[0] = True

	for i in range(m):
		x, y = map(int, input().split())
		d[x].append(y)
		d_transpose[y].append(x)


	lst = list()
	for i in range(1, n + 1):
		if not visited[i]:
			dfs(d, i, visited, lst)


	visited = [False] * (n + 1)
	visited[0] = True

	cnt = 0
	while lst:
		top = lst.pop()
		if not visited[top]:
			dfs_reverse(d_transpose, top, visited)
			cnt += 1

	print(cnt)


if __name__ == '__main__':
	main()