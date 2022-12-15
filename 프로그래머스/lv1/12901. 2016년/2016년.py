def solution(a, b):
    mdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU','FRI','SAT', 'SUN','MON','TUE','WED']
    
    answer = days[( sum(mdays[:a-1]) + b ) % 7]
    
    return answer