from itertools import combinations

def solution(nums):
    ans = min(len(nums) // 2, len(set(nums)))
    
    return ans