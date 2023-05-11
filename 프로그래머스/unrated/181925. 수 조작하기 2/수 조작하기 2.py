def solution(numLog):
    d = {1:'w', -1:'s', 10:'d', -10:'a'}
    f = lambda x : x[1]-x[0]
    res = []
    for i in range(len(numLog)-1):
        res.append(d.get(f(numLog[i:i+2])))
    return ''.join(res)