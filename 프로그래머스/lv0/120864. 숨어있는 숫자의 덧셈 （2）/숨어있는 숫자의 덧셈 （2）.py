def solution(my_string):
    my_string = my_string.lower()
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', ' '*26)
    return sum([int(i) for i in my_string.translate(table).split(' ') if i != ''])