def solution(array, commands):
    li=[]
    for j in commands:
        li.append(sorted([i for i in array][j[0]-1:j[1]])[j[2]-1])
    return li