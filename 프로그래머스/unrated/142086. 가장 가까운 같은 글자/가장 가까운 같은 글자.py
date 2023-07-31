def solution(s):
    res = []
    b = []    
    for i in s:
        if i not in b:
            res.append(-1)
        else:
            pos = b[::-1].index(i)+1
            res.append(pos)
        b.append(i)
    return res