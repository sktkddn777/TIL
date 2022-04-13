
'''
조합으로 푸는 방법
'''
from itertools import permutations

def track_dungeon(case, dungeons, k):
	num = 0

	for c in case:
		if dungeons[c][0] > k:
			return num
		k -= dungeons[c][1]
		num += 1
	return num

def solution(k, dungeons):
	dungeon_lst = [x for x in range(len(dungeons))]
	cases = list(permutations(dungeon_lst, len(dungeon_lst)))
	
	ans = 0
	for case in cases:
		n = track_dungeon(case, dungeons, k)
		if n > ans:
			ans = n
	return ans
			
print(solution(80, [[80,20],[50,40],[30,10]]))


'''
백트래킹으로 푸는 방법.
'''

ans = 0

def dfs(k, dungeons, visited, cnt):
	global ans
	if cnt > ans:
		ans = cnt
	
	for i in range(len(dungeons)):
		if k >= dungeons[i][0] and visited[i] == 0:
			visited[i] = 1
			dfs(k-dungeons[i][1], dungeons, visited, cnt + 1)
			visited[i] = 0

def solution(k, dungeons):
	n = len(dungeons)
	visited = [0] * n
	dfs(k, dungeons, visited, 0)
	return ans