def solution(num):
    cnt=0
    k=lambda x : x/2 if x%2==0 else x*3+1
    while(num!=1): 
        cnt+=1
        if cnt == 500:
            return -1
        num=k(num)
    return cnt