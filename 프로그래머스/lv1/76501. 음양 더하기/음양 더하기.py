def solution(absolutes, signs):
    k=list(map(lambda x:1 if x==True else -1, signs))
    return sum([(i*j) for i,j in zip(absolutes,k)])