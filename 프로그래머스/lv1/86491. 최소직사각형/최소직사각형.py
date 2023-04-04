def solution(sizes):
    m=[]
    s=[]
    for i in sizes:
        i.sort()
        s.append(i[0])
        m.append(i[1])

    return max(m)*max(s)