def primenumber(x):
    for i in range (2, int((x**0.5) + 1)):
        if x % i == 0:
            return False
    return True                    

def solution(n):
    res=0
    li=[i for i in range(2,n+1)]
    
    for i in li:
        if primenumber(i):
            res+=1

    return res