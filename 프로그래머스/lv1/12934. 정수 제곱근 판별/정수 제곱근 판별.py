def solution(n):
    x = n ** 0.5
    
    if int(x) == x:
        return (x + 1) ** 2
    else:
        return -1