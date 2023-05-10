def solution(arr, k):
    return [i*k if bool(k%2) else i+k for i in arr]