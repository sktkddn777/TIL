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

# 11/15 다시 풀어봤는데 규칙을 찾지 못해서 다시 풀이를 보고 풀었다.
'''
def find_num(num):
    bin_num = list(bin(num)[::-1][:-2])

    if num % 2 == 0:
        bin_num[0] = '1'
    else:
        try:
            idx=bin_num.index('0')
            bin_num[idx] = '1'
            bin_num[idx-1] = '0'
        except ValueError:
            bin_num.append('1')
            bin_num[-2] = '0'

    return ''.join(bin_num[::-1])

def solution(numbers):
    result = []
    for number in numbers:
        a = int(find_num(number),2)
        result.append(a)
    return result
'''