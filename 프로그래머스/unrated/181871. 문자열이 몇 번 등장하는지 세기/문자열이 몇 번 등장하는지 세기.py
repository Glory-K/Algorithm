def solution(myString, pat):
    return sum([True if pat in myString[i:i+len(pat)] else False for i in range(len(myString))])