def solution(strings, n):
    words=[i for i in strings]
    words=sorted(words)
    return sorted(words, key=lambda x : x[n])