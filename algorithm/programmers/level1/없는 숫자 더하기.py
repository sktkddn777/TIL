def solution(numbers):
    num_lst = [x for x in range(10)]
    for num in numbers:
        num_lst.remove(num)
    
    answer = sum(num_lst)
    return answer