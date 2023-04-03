T=input()
datas=[]
for i in range(int(T)):
    datas.append(input())
    
for data in datas:
    cnt=0
    res='YES'
    for i in data:
        if i == '(':
            cnt+=1
        else:
            cnt-=1
        
        if cnt==-1:
            res='NO'
            break
    if cnt != 0:
        res='NO'
    print(res)
