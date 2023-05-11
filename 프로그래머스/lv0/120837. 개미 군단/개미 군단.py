def solution(hp):
    cnt = 0
    ants = [5, 3, 1]
    for ant in ants:
        cnt+= hp//ant
        hp -= (ant * (hp//ant))
    
    return cnt