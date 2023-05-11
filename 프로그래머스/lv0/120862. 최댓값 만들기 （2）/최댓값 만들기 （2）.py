def solution(numbers):
    m = -10000**2
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            s = numbers[i] * numbers[j]
            if s >= m: m = s
    return m                    