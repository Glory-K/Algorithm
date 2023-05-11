def solution(arr, flag):
    X = []
    for idx, i in enumerate(arr):
        if flag[idx]:
            for j in range(i*2):
                X.append(i)
        else:
            X = X[:-i]
    return X