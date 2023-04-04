a, b = map(int, input().strip().split(' '))

def solution(a,b):
    k='*'*a
    for i in range(b):
        print(k)
solution(a,b)