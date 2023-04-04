def solution(n):
    a=[]
    while n>0:
        s=n%3
        n//=3
        a.append(s)
    return sum([(i*(3**(idx)//3)) for idx, i in enumerate(a[::-1],start=1)])