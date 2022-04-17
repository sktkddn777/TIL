from collections import Counter

def solution(a):
	if len(a) < 2:
		return 0
	
	counter = Counter(a)
	res = 0
	for k,v in counter.items():
		idx = 0
		tmp = 0
		if v > res:
			while idx < len(a)-1:
				if (a[idx] == k or a[idx+1] == k) and a[idx] != a[idx+1]:
					idx += 2
					tmp += 1
				else:
					idx += 1
		if tmp > res:
			res = tmp
	return res * 2


solution([0,3,3,0,7,2,0,2,2,0])