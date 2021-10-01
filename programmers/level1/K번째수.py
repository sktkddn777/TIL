def solution(array, commands):
    answer = []

    for data in commands:
        new_array = array[data[0] - 1: data[1]]
        new_array.sort()
        answer.append(new_array[data[2] - 1])
    return answer