def solution(emergency):
    e = sorted(emergency, reverse=True)

    res = []
    for i in emergency:
        res.append(e.index(i)+1)

    return res