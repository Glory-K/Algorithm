def solution(arr):
    cnt=0
    l = len(arr)
    for i in range(l):
        for j in range(l):
            if arr[i][j]==arr[j][i]:
                cnt+=1
    return 1 if cnt==l**2 else 0