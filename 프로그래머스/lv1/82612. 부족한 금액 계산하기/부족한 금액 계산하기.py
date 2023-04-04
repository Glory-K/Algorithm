def solution(price, money, count):
    total=sum([i for i in range(price, price*count+1) if i % price==0])
    res=total-money
    return res if total>money else 0