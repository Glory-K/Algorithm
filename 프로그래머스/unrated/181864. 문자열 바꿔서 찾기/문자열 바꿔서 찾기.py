def solution(myString, pat):
    pat = ['B' if i=='A' else 'A' for i in pat]
    return int(''.join(pat) in myString)