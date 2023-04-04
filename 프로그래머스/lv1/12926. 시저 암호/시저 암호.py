def solution(s,n):
    num_alpha=[ord(i) for i in s]
    res=[]
    
    for i in num_alpha:
        if chr(i).isupper():
            res.append(chr(65+((i+n)-65)%26))
        elif chr(i).islower():
            res.append(chr(97+((i+n)-97)%26))
        else:
            res.append(chr(i))
    return "".join(res)