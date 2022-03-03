def solution(new_id):
    # 1단계
    lower = new_id.lower()

    txt = ""
    dot = ''

    # 2, 3 단계
    for l in lower:
        asc = ord(l)
        if 97 <= asc <= 122 or asc == 45 or asc == 95 or 48 <= asc <= 57:
            txt += l
            dot = l
        elif asc == 46:
            if dot != '.':
                txt += l
            dot = l

    # 4단계
    if len(txt) > 0:
        if txt[0] == '.':
            txt = txt[1:]
    if len(txt) > 0:
        if txt[-1] == '.':
            txt = txt[:-1]

    # 5단계
    if len(txt) == 0:
        txt = "a"

    # 6단계
    if len(txt) >= 16:
        txt = txt[:15]

    if txt[-1] == '.':
        txt = txt[:-1]

    # 7단계
    if len(txt) <= 2:
        word = txt[-1]
        while len(txt) < 3:
            txt += word
    
    return txt