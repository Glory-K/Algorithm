def solution(num_list):
    res = 0
    for i in num_list:
        cnt = 0
        while True:
            if i == 1:
                res+=cnt
                break
            if i%2==0:
                i/=2
            else:
                i=(i-1)/2
            cnt+=1
    return res