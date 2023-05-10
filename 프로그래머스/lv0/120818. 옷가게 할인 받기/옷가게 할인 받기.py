def solution(price):
    if price >= 500000:
        res = price*80/100
    elif price >= 300000:
        res = price*90/100
    elif price >= 100000:
        res =  price*95/100
    else:
        res = price
        
    return int(res)