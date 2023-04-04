def solution(n, m):
    for i in range(max(n,m), n*m+1):
        if i%n==0 and i%m==0:
            a=i
            break
    
    for i in range(max(n,m), 0, -1):
        if n%i==0 and m%i==0:
            b=i
            break
    return [b,a]