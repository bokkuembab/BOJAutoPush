import sys
input = sys.stdin.readline

n, l = map(int, input().split())
nums = []    # 수열

def backtracking():

    # 종료 조건
    if len(nums) == l:
        print(' '.join(map(str, nums)))
        return
    
    # 수열 중복 방지
    if nums: now = nums[-1]
    else: now = 1
    
    # 현재 숫자 ~ n까지 반복
    for i in range(now, n + 1):
        nums.append(i)
        backtracking()
        nums.pop()

backtracking()