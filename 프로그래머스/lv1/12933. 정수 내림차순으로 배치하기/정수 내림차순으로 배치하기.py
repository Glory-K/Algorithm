def solution(n):
    # x=[i for i in str(n)]
    # x.sort(reverse=True)
    # re=str()
    # for j in x:
    #     re+=j
    # return int(re)
    return int("".join(sorted([n for n in str(n)], reverse=True)))



