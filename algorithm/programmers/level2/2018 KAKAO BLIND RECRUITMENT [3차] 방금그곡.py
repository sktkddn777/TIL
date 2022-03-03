def change_alp(word_lst):
    note = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for word in note:
        if word in word_lst:
            word_lst = word_lst.replace(word, note[word])
    return word_lst


def sub_time(t1, t2):
    t1 = t1.split(':')
    t2 = t2.split(':')
    return (int(t2[0]) - int(t1[0])) * 60 + (int(t2[1]) - int(t1[1]))


def solution(m, musicinfos):
    answer = []
    m = change_alp(m)
    for i, musicinfo in enumerate(musicinfos):
        lst = musicinfo.split(',')
        time = sub_time(lst[0], lst[1])
        word = change_alp(lst[3])

        if time >= len(word):
            word = (time // len(word)) * word + word[:time % len(word)]
        else:
            word = word[:time]

        if m in word:
            answer.append((lst[2], time, i))
    if answer:
        answer.sort(key=lambda x: (-x[1], x[2]))
        return answer[0][0]
    return '(None)'