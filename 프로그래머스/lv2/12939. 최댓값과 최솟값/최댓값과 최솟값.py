def solution(s):
    num=s.split(' ')
    num=[int(i) for i in num]
    return str(min(num))+' '+str(max(num))