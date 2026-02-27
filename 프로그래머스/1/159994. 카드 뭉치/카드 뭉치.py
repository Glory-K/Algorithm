def solution(cards1, cards2, goal):
    x, y = 0, 0
    
    for word in goal:
        if x < len(cards1) and cards1[x] == word:
            x += 1
        elif y < len(cards2) and cards2[y] == word:
            y += 1
        else:
            return "No"
    
    return "Yes"