def solution(n):
    word = '수박'
    if n % 2 == 0:
        return word*(n//2)
    else:
        return word*(n//2) + word[n%2 - 1]