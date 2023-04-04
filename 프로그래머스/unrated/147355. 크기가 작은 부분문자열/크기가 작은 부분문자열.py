def solution(t, p):
    res=[]
    for i in range(0,len(t)):
        if len(t[i:i+len(p)]) < len(p):
            break
        res.append(t[i:i+len(p)])
    
    return len([i for i in res if i <= p])