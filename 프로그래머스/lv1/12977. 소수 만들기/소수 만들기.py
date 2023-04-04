def get_measure(num):
    res=[]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            if num // i != i:
                res.append(num//i)
    return len(res)


def solution(nums):
    cnt=0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if 0==get_measure(nums[i]+nums[j]+nums[k]):
                    cnt+=1
        
    return cnt