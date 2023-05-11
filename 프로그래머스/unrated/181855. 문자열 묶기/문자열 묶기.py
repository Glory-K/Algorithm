def solution(strArr): 
    strArr = [len(i) for i in strArr]
    d = {}
    m=-1
    for i in set(strArr):
        if m<strArr.count(i):
            m=strArr.count(i)
    return m