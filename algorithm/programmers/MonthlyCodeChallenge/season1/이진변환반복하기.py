
def solution(s):
    iterate_count = 0
    zero_count = 0

    while s != '1':
        zero_count += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
        iterate_count += 1

    return [iterate_count, zero_count]

solution("110010101001")