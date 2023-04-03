from collections import Counter

def solution(participant, completion):
    dic = Counter(participant)

    for i in completion:
        if i in dic and dic.get(i) != 0:
            dic[i] = dic.get(i) - 1

    for i, j in dic.items():
        if j == 1:
            return i