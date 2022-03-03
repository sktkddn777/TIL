def solution(genres, plays):
    answer = []
    sum_song = {}
    song = {}

    for i, genre in enumerate(genres):
        song[genre] = song.get(genre, []) + [(plays[i], i)]
        sum_song[genre] = sum_song.get(genre, 0) + plays[i]

    sum_song = sorted(sum_song.items(), key=lambda x:x[1], reverse=True)

    for key, value in song.items():
        song[key] = sorted(value, key=lambda x:x[0], reverse=True)[:2]

    for s in sum_song:
        answer.extend(x[1] for x in song[s[0]])
    return answer