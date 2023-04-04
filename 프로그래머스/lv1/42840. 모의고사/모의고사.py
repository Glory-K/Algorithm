def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    k=[a]+[b]+[c]
    ms=[]
    for i in k:
        so=i * int(len(answers)//len(a) + 1)
        so=so[:len(answers)]
        ms.append(sum([so[m]==answers[m] for m in range(len(so))]))
    return sorted([idx+1 for idx,i in enumerate(ms) if i==max(ms)])