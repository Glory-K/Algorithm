# 빈 병 20개 중 18개를 마트에 가져가서, 6병의 콜라를 받습니다. 
# 이때 상빈이가 가지고 있는 콜라 병의 수는 8(20 – 18 + 6 = 8)개 입니다.

# a개 가져다주면 b개 준다

def solution(a, b, n):
    answer = 0
    
    while True:
        if n // a == 0:
            break

        receive = b * (n // a)
        remain = (n % a) + receive
        answer+=receive
        n = remain

    return answer