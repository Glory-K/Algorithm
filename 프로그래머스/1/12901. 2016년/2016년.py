def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31]
    days = sum(month[:a-1]) + b
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    return week[days % 7]