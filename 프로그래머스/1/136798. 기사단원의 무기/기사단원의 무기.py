def solution(number, limit, power):
    divisor = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisor[j] += 1
    
    result = 0
    
    for i in range(1, number + 1):
        if divisor[i] > limit:
            result += power
        else:
            result += divisor[i]
    
    return result