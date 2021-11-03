from collections import deque


def check(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    return diff


def solution(begin, target, words):

    def bfs():
        queue = deque([begin])
        visited = [0] * len(words)

        while queue:
            data = queue.popleft()

            lst_data = list(data)
            for i, word in enumerate(words):
                lst_word = list(word)
                if check(lst_word, lst_data) == 1 and visited[i] == 0:
                    try:
                        visited[i] = visited[words.index(data)] + 1
                    except ValueError:
                        visited[i] = 1

                    queue.append(word)

        return visited[words.index(target)]

    if target in words:
        return bfs()
    return 0