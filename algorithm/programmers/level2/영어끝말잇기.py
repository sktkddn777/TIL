from math import ceil
def solution(n, words):
    stack = [words[0]]
    number = 1

    for word in words[1:]:
        number += 1
        if stack[-1][-1] != word[0]:
            break

        if word in stack:
            break

        stack.append(word)

    if len(stack) == len(words):
        return [0, 0]

    if number%n == 0:
        return [n, ceil(number/n)]
    return [number%n, ceil(number/n)]