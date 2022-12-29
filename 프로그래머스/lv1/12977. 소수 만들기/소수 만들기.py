from itertools import combinations

def solution(nums):
    answer = 0
    
    for s in list(sum(c) for c in combinations(nums, 3)):
        for i in range(2, int(s ** 0.5) + 1):
            if s % i == 0:
                break
        else:
            answer += 1

    return answer