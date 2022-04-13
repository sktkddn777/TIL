def solution(sizes):
	garo, sero = 0, 0

	for size in sizes:
		if size[0] > garo or size[1] > sero:
			x = abs(size[0] - garo) + abs(size[1] - sero)
			y = abs(size[0] - sero) + abs(size[1] - garo)
			tmp_g, tmp_s = garo, sero
			if x < y:
				garo = max(size[0], tmp_g)
				sero = max(size[1], tmp_s)
			else:
				garo = max(size[0], tmp_s)
				sero = max(size[1], tmp_g)
	return garo * sero
	
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))