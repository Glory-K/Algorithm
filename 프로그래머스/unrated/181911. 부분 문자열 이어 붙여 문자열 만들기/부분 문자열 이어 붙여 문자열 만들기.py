def solution(my_strings, parts):
    return ''.join([string[parts[i][0]:parts[i][1]+1] for i, string in enumerate(my_strings)])