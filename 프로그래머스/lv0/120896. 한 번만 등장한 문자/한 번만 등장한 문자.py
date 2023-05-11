def solution(s):
    d = {}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return ''.join(sorted([list(d.keys())[idx] for idx, i in enumerate(d.values()) if i==1]))