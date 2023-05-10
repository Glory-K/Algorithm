def solution(numbers, n):
    res=0
    for i in numbers:
        if res <= n:
            res+=i
        else:
            break
        
    return res