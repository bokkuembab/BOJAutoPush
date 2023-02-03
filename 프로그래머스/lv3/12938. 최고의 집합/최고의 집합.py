def solution(n, s):
    ans = []
    
    if s // n == 0:
        return [-1]
    
    if s % n == 0:
        return [s // n] * n
    else:
        while n >= 1:
            ans.append(s // n)
            s -= s // n
            n -= 1
    
    return ans