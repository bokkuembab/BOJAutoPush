def times(n):
    t = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            t += 2
            
    if int(n ** 0.5) == n ** 0.5:
        t -= 1
        
    return t % 2 == 0

def solution(left, right):
    
    return sum(x if times(x) else -x for x in range(left, right + 1))