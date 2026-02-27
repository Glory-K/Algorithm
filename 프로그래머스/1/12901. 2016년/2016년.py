def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31]
    
    date = 0
    
    for i in range(0, a-1):
        date+=month[i]
    
    date+=b
    day = date%7
    print(date, day)
    day_eng=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    return day_eng[day]