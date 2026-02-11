def solution(n):
    res = 1
    for i in range(1, n):
        for a in range(1, n):
            s = sum(range(1, a)) + a * i 
            if s == n:
                res += 1
                break
            elif s > n:
                break
            
    return res