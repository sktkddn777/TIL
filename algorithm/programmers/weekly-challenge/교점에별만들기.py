from itertools import combinations

def make_star(star_lst):
	min_x = min([x[0] for x in star_lst])
	max_x = max([x[0] for x in star_lst])
	min_y = min([x[1] for x in star_lst])
	max_y = max([x[1] for x in star_lst])

	output = [['.'] * (max_x - min_x + 1) for _ in range((max_y - min_y + 1))]

	for s in star_lst:
		x, y = s
		nx = x + abs(min_x) if min_x < 0 else x - min_x
		ny = y + abs(min_y) if min_y < 0 else y - min_y
		output[ny][nx] = '*'
	return [''.join(x) for x in output]

def solution(line):
	line_idx = [x for x in range(len(line))]
	cases = list(combinations(line_idx, 2))
	meet_point = []

	for case in cases:
		A, B, E = line[case[0]]
		C, D, F = line[case[1]]
		if ((A*D) - (B*C)) != 0:
			x = ((B*F)-(E*D)) / ((A*D)-(B*C))
			y = ((E*C)-(A*F)) / ((A*D)-(B*C))
			if x == int(x) and y == int(y):
				meet_point.append([int(x), int(y)])

	return make_star(meet_point)


lst = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(lst))