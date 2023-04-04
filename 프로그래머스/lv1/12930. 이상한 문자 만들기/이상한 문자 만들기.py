def solution(s):
    str_li=[i for i in s]
    cnt=0
    res=[]
    for i in str_li:
        cnt+=1
        if i == ' ':
            cnt=0
        if cnt%2==1:
            res.append(i.upper())
        else:
            res.append(i.lower())
    return "".join(res)