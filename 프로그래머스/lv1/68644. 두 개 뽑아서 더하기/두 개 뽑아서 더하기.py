from itertools import combinations

def solution(numbers):
    answer = list(set(sum(c) for c in combinations(numbers, 2)))
    
    return sorted(answer)