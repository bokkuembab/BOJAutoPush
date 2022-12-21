from itertools import combinations

def solution(numbers):
    answer = set(sum(c) for c in combinations(numbers, 2))
    answer = list(answer)
    
    return sorted(answer)