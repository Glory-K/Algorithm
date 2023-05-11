def solution(numbers):
    number_table = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    k = ''
    res = ''
    for i in numbers:
        k+=i
        if k in number_table.keys():
            print(res)
            res+=str(number_table.get(k))
            k=''
    return int(res)