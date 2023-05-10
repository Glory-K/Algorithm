def solution(n, control):
    w = control.count('w')
    s = control.count('s') * -1
    d = control.count('d') * 10
    a = control.count('a') * -10
    
    
    return n+w+s+d+a