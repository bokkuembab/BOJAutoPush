def solution(n):
    
    if n == 1:
        return n % 1234567
    elif n == 2:
        return n % 1234567
    else:
        bf, ans = 1, 2
        for _ in range(n-2):
            bf, ans = ans, bf+ans
    return ans % 1234567