def solution(arr):
    res=[]
    for i in arr:
        for j in range(i):
            res.append(i)
    return res