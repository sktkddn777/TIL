vowels = ['A', 'E', 'I', 'O', 'U']

c = 0
res = 0
def dfs(lst, word):
    global res, c
    if lst == word:
        res = c

    if len(lst) == 5:
        return

    for vowel in vowels:
        lst.append(vowel)
        c += 1
        dfs(lst, word)
        lst.pop()

def solution(word):
    word = list(word)
    dfs([], word)
    return res

print(solution("AAAE"))