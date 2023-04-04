from itertools import combinations

def solution(numbers):
    c=list(combinations(numbers,2))
    print(c)
    return list(sorted(set(map(lambda x:x[0]+x[1], c))))