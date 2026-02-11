def solution(s):
    q = []
    
    for i in s:
        if i == '(':
            q.append(i)
        elif i == ')':
            try:
                q.pop()
            except:
                return False
    if len(q) == 0:
        return True
    
    return False