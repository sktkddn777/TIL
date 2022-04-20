def solution(numbers):
    lst = [x for x in range(10)]
    for number in numbers:
        lst.remove(number)
    return sum(lst)

print(solution([5, 8, 4, 0, 6, 7, 9]))