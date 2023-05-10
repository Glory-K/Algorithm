def solution(num_list):
    res = 1
    for i in num_list:
        res*=i
    
    return sum(num_list) if len(num_list) >= 11 else res