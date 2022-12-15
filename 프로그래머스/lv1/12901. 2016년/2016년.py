def solution(a, b):
    mdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU','FRI','SAT', 'SUN','MON','TUE','WED']
    
    total_days = 0
    for i in range(a - 1):
        total_days += mdays[i]
    total_days += b
    
    return days[total_days % 7]