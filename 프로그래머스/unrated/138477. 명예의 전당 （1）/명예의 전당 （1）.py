def solution(k, score):
    answer = []
    a = []
    
    for i in score:
        a.append(i)
        a = sorted(a)[::-1]
        if len(a) > k:
            a.pop(-1)
        answer.append(a[-1])
    return answer