def solution(s):
    answer=[]
    cnt=0
    for i in s:
        if i == ' ':
            cnt=-1
        if cnt==0:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
        cnt+=1
    return "".join(answer)