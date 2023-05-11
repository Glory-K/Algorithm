def solution(a, d, included):
    res = 0
    for idx, i in enumerate(range(a, a+(len(included)-1)*d+1, d)):
        if included[idx]:
            res+=i
    return res