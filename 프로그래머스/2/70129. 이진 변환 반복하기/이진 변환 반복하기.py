def solution(s):
    cycle = 0
    count_zero = 0
    
    while True:
        if len(s) > 1:
            if s.count("0") > 0:
                count_zero += s.count("0")
                s = s.replace("0","")

            s = bin(len(s))[2:]
            cycle += 1
        else:
            return [cycle, count_zero]

    return -1