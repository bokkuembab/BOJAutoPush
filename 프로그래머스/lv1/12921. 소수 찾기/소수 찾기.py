def is_prime(num):
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def solution(n):
    ans = [0] * (n + 1)
    
    for num in range(2, n + 1):
        if ans[num] == 1:
            continue
        ans[num] = is_prime(num)
        
    return sum(ans)