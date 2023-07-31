# 1번 3개
# 2번 4개
# 3번 6개
def solution(food):
    a = [i//2 for i in food[1:]]
    res = []
    for idx, i in enumerate(a):
        for j in range(i):
            res.append(idx+1)
    res = res + [0] + res[::-1]
    
    return ''.join(map(str, res))
