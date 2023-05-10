def solution(num_list):
    res = 1
    for i in num_list:
        res*=i
    
    return int(sum(num_list)**2 > res)