def solution(numbers):
    res = []
    for number in numbers:
        bin_num = bin(number)[2:]
        if bin_num[-1] == '0':
            bin_num = bin_num[:-1] + '1'
            
        else:
            bin_num = list('0' + bin_num)[::-1]
            
            for i in range(len(bin_num)):
                if bin_num[i] == '0':
                    bin_num[i] = '1'
                    bin_num[i-1] = '0'
                    break
            bin_num = ''.join(bin_num[::-1])
        res.append(int(bin_num, 2))

    return res

print(solution([2, 7]))