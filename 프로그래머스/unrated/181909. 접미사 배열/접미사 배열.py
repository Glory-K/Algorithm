def solution(my_string):
    res=[]
    for i in range(len(my_string)):
        res.append(my_string[i:])
    return sorted(res)