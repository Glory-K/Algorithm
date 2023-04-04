def solution(arr, divisor):
    k = [i for i in arr if i%divisor==0]
    k.sort()
    return k if k != [] else [-1]