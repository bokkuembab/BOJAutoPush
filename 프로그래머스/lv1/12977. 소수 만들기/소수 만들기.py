from itertools import combinations

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    
    for s in list(sum(c) for c in combinations(nums, 3)):
        answer += is_prime(s)

    return answer