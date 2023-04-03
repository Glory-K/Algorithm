N=int(input())
res=[]
def binary(N):
    if N != 0:
        res.append(N%2)
        binary(N//2)
    return res
res=binary(N)
res.reverse()
print(''.join([str(i) for i in res]))