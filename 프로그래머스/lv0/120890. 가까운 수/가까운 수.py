def solution(array, n):
    array.sort()
    m=999
    for i in array:
        print(i , abs(n-i))
        if m > abs(n-i):
            m = abs(n-i)
            res=i
    return res