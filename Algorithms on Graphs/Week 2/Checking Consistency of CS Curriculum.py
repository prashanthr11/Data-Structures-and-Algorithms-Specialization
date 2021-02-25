from collections import defaultdict as dt


def dfs(s, l, d):
	if not d[s]:
		return False
		

	for i in d[s]:
		if i in l:
			return True

		if dfs(i, l + [s], d):
		    return True

	return False


def solve(n, m):
	d = dt(list)
	for i in range(m):
		x, y = map(int, input().split())
		d[x].append(y)
	
	for i in range(1, n + 1):
	    if dfs(i, [], d):
	        return 1
	
	return 0
	  

n, m = map(int, input().split())
print(solve(n, m))