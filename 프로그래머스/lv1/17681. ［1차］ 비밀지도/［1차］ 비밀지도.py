def solution(n, arr1, arr2):
    ar1=[]
    ar2=[]
    for i,j in zip(arr1, arr2):
        ar1.append(bin(i)[-n:].replace('b','0').zfill(n))
        ar2.append(bin(j)[-n:].replace('b','0').zfill(n))
    total=[]

    a=''
    for i in range(n**2):
        a+="".join('#' if max(ar1[i//n][i%n], ar2[i//n][i%n])=='1' else ' ')
        if i%n==(n-1):
            print(a)
            total.append(a)
            a='' 
    return total