def solution(my_string):
    return sum([int(i) if i.isnumeric() else 0 for i in my_string])