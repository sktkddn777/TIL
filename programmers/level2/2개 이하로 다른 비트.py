'''
하나하나 비교하려니까 시간초과가 났다.

구글링을 통해 다른 사람의 풀이를 참조했다.
'''

def find_num(num):
    binary = list(bin(num)[::-1][:-2])

    if num % 2 == 0:
        binary[0] = '1'
    else:
        try:
            index = binary.index('0')
            binary[index] = '1'
            binary[index-1] = '0'
        except ValueError:
            binary[-1] = '0'
            binary.append('1')

    return int(''.join(binary[::-1]), 2)


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(find_num(number))

    return answer