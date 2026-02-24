def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    attack_turn = False
    bandage_cnt = 0
    turn = 0
    
    while True:
        if attacks[0][0] == turn:
            attack = attacks.pop(0)
            attack_turn = True

        if attack_turn:
            health -= attack[-1]
            attack_turn = False
            
            if health <= 0:
                return -1
            else:
                bandage_cnt = 0
                
        else:
            health += x
            bandage_cnt += 1
            if bandage_cnt == t:
                bandage_cnt = 0
                health += y
            if health > max_health:
                health = max_health
        
        if len(attacks) == 0:
            return health
        turn+=1
    return 0
