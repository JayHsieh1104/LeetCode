def solution(riddle):
    n = len(riddle)
    res = 'a'
    if riddle == "?":
        return "a"

    if riddle[0] == "?" and riddle[1] != "?":
        if riddle[1] == "z":
            res += "a"
        else:
            res += chr(ord(riddle[1]) + 1)

    for i in range(1, n-1):
        if riddle[i+1] == "?":
            res += chr(ord(riddle[i]) + 1)     
        else:
            res += riddle[i+1]
    print(res)

    return riddle

solution("ab?ac?")