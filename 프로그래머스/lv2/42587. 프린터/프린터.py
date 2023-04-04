def solution(priorities, location):
    res = 0

    while(True):
        m = max(priorities)
        q = priorities.pop(0)
        if q == m:
            res += 1
            if location == 0:
                break
            else:
                location-=1
        else:
            priorities.append(q)
            if location == 0:
                location=len(priorities)-1
            else:
                location-=1

    return res